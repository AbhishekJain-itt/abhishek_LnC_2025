package com.atm.service;

import com.atm.controller.ATMDeviceController;
import com.atm.exception.*;

public class ATMService {

    public void processWithdrawal(String accountId, double amount) {

        ATMDeviceController controller = new ATMDeviceController();

        try {

            controller.withdraw(accountId, amount);

            System.out.println("Withdrawal successful");

        } catch (DeviceLockedException e) {

            System.out.println("ATM device is locked");

        } catch (NetworkConnectionException e) {

            System.out.println("Network issue occurred");

        } catch (InsufficientFundsException e) {

            System.out.println("Insufficient balance");

        } catch (DeviceNotFoundException e) {

            System.out.println("ATM device unavailable");

        }
    }
}
