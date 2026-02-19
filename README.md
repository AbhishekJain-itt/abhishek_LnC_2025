# Law of Demeter Refactoring – Payment Collection System

## Overview

This project demonstrates a practical refactoring exercise focused on applying:

- The **Law of Demeter**
- The **Tell, Don’t Ask** principle
- Proper object-oriented design
- Clean Code principles (SRP, encapsulation, intention-revealing names)

The goal was to eliminate "train wreck" method calls and prevent exposure of internal object structures.

---

## Problem (Before Refactoring)

The `Paperboy` class accessed the internal `Wallet` of `Customer` directly:

```java
Wallet wallet = customer.getWallet();
if (wallet.getTotalMoney() >= paymentAmount) {
    wallet.subtractMoney(paymentAmount);
}
```

Issues:

- Violates Law of Demeter

- Breaks encapsulation

- Exposes implementation details

- Creates tight coupling

- Treats objects like data structures

# Refactored Design (After)

Now, the Paperboy simply tells the Customer to pay:

customer.pay(amount);

# Improvements:

- No internal navigation

- No wallet exposure

- Clear separation of responsibilities

- Objects expose behavior, not data
