# ATM Refactoring – Exceptions vs Error Codes

## Overview

This assignment demonstrates how to refactor a poorly structured ATM withdrawal system that uses **error codes and nested conditional logic** into a cleaner design using **exceptions and clear business flow**.

The refactoring follows principles from **Clean Code** and focuses on:

* Eliminating error codes
* Using custom exceptions
* Separating business logic from error handling
* Making the main workflow readable (Happy Path)
* Following proper Java naming conventions

---

## Problem in the Original Code

The original implementation used **error codes** such as:

* `-1 → DEVICE_SUSPENDED`
* `-2 → INSUFFICIENT_FUNDS`
* `-3 → CONNECTION_ERROR`

This approach caused several issues:

* Deeply nested `if` conditions
* Business logic mixed with error handling
* Poor readability
* Hard-to-maintain code
* Magic numbers instead of meaningful errors

Example of problematic structure:

```
if (...)
  if (...)
    if (...)
      if (...)
```

This makes the code difficult to understand and maintain.

---

## Refactoring Goals

The refactoring improves the design by:

1. **Removing error codes**
2. **Introducing custom exceptions**
3. **Separating business logic from error handling**
4. **Improving readability through the Happy Path pattern**
5. **Breaking logic into small single-responsibility methods**

---

## Project Structure

```
src/
 └── com/
     └── atm/
         ├── controller/
         │     └── ATMDeviceController.java
         │
         ├── service/
         │     └── ATMService.java
         │
         ├── exception/
              ├── DeviceLockedException.java
              ├── InsufficientFundsException.java
              ├── NetworkConnectionException.java
              └── DeviceNotFoundException.java
       
```

---

## Key Design Improvements

### 1. Custom Exceptions

Instead of returning error codes, the system throws meaningful exceptions.

Examples:

* `DeviceLockedException`
* `InsufficientFundsException`
* `NetworkConnectionException`
* `DeviceNotFoundException`

This improves readability and error traceability.

---

### 2. Happy Path Business Logic

The main withdrawal flow is now easy to read:

```
withdraw()
 → fetchDeviceHandle()
 → fetchDeviceRecord()
 → validateDeviceStatus()
 → validateNetworkConnection()
 → validateAccountBalance()
 → dispenseCash()
```

This makes the business logic **self-explanatory**.

---

### 3. Separation of Concerns

| Layer      | Responsibility                   |
| ---------- | -------------------------------- |
| controller | Business logic                   |
| service    | Error handling and orchestration |
| model      | Data structures                  |
| exception  | Failure scenarios                |

This follows **Clean Architecture principles**.

---

## Benefits of Refactoring

* Improved readability
* Better maintainability
* Clear error handling
* Reduced complexity
* Easier debugging
* More scalable architecture

---

## Concepts Demonstrated

* Clean Code principles
* Exception-based error handling
* Happy Path design
* Single Responsibility Principle
* Separation of concerns

---

## Conclusion

By replacing error codes with exceptions and separating concerns, the ATM withdrawal system becomes significantly more readable and maintainable.

This refactoring highlights how **clean architecture and exception handling improve real-world software systems.**
