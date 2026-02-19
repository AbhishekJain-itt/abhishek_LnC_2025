package com.delivery;

public class Paperboy {
    public void collectPaymentFrom(Customer customer, double amount) {
        boolean paymentSuccessful = customer.pay(amount);

        if (!paymentSuccessful) {
            scheduleFollowUpVisit();
        }
    }

    private void scheduleFollowUpVisit() {
        // Retry logic
    }
}
