package com.delivery;

public class Wallet {

    private double balance;

    public Wallet(double initialBalance) {
        this.balance = initialBalance;
    }

    public boolean debit(double amount) {
        if (!hasSufficientFunds(amount)) {
            return false;
        }

        balance -= amount;
        return true;
    }

    private boolean hasSufficientFunds(double amount) {
        return balance >= amount;
    }
}
