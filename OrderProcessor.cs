public class OrderProcessor
{
    private readonly IPaymentGateway paymentGateway;
    private readonly IInventoryService inventoryService;
    private readonly INotificationService notificationService;

    public OrderProcessor(
        IPaymentGateway paymentGateway,
        IInventoryService inventoryService,
        INotificationService notificationService)
    {
        this.paymentGateway = paymentGateway;
        this.inventoryService = inventoryService;
        this.notificationService = notificationService;
    }

    public async Task<OrderResult> ProcessOrderAsync(Order order)
    {
        ValidateOrderArgument(order);

        if (!IsOrderEligibleForProcessing(order))
        {
            return OrderResult.Invalid("Order validation failed.");
        }

        if (!await inventoryService.IsInventoryAvailableAsync(order.Items))
        {
            return OrderResult.Failed("Insufficient inventory.");
        }

        await inventoryService.ReserveItemsAsync(order.Items);

        return await ProcessPaymentAndFinalizeOrderAsync(order);
    }

    private async Task<OrderResult> ProcessPaymentAndFinalizeOrderAsync(Order order)
    {
        try
        {
            var paymentResult = await paymentGateway.ProcessPayment(
                order.CustomerId,
                order.TotalAmount,
                order.PaymentMethod);

            return paymentResult.IsSuccessful
                ? await CompleteSuccessfulOrderAsync(order, paymentResult.TransactionId)
                : await HandleFailedPaymentAsync(order, paymentResult.ErrorMessage);
        }
        catch
        {
            await inventoryService.ReleaseReservationAsync(order.Items);
            throw;
        }
    }

    private async Task<OrderResult> CompleteSuccessfulOrderAsync(Order order, string transactionId)
    {
        await inventoryService.CommitReservationAsync(order.Items);
        await notificationService.SendOrderConfirmationAsync(order);

        return OrderResult.Success(transactionId);
    }

    private async Task<OrderResult> HandleFailedPaymentAsync(Order order, string errorMessage)
    {
        await inventoryService.ReleaseReservationAsync(order.Items);
        return OrderResult.Failed($"Payment failed: {errorMessage}");
    }

    private static void ValidateOrderArgument(Order order)
    {
        if (order == null)
        {
            throw new ArgumentNullException(nameof(order));
        }
    }

    private static bool IsOrderEligibleForProcessing(Order order)
    {
        return order.Items is { Count: > 0 } && order.TotalAmount > 0;
    }

    public async Task CancelOrderAsync(string orderId)
    {
        var order = await LoadOrderAsync(orderId);

        if (order.Status == OrderStatus.Paid)
        {
            await RefundAndRestoreInventoryAsync(order);
        }

        order.Status = OrderStatus.Cancelled;
        await PersistOrderAsync(order);
    }

    private async Task RefundAndRestoreInventoryAsync(Order order)
    {
        await paymentGateway.RefundPayment(order.TransactionId);
        await inventoryService.RestoreInventoryAsync(order.Items);
    }

    private Task<Order> LoadOrderAsync(string orderId)
    {
        // Data access implementation belongs here
        return Task.FromResult(new Order());
    }

    private Task PersistOrderAsync(Order order)
    {
        // Data persistence implementation belongs here
        return Task.CompletedTask;
    }
}
