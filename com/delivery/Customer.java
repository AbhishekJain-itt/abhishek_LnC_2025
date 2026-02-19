package com.delivery;

public class Customer {

    private final String firstName;
    private final String lastName;
    private final Wallet wallet;

    public Customer(String firstName, String lastName, Wallet wallet) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.wallet = wallet;
    }

    public boolean pay(double amount) {
        return wallet.debit(amount);
    }

    public String getFullName() {
        return firstName + " " + lastName;
    }
}
