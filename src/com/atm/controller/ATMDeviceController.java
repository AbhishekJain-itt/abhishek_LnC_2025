package com.atm.controller;

import com.atm.exception.*;

public class ATMDeviceController {

    public void withdraw(String accountId, double amount) throws DeviceLockedException,InsufficientFundsException,NetworkConnectionException,DeviceNotFoundException {

        DeviceHandle handle = fetchDeviceHandle();

        DeviceRecord record = fetchDeviceRecord(handle);

        validateDeviceStatus(record);

        validateNetworkConnection(record);

        validateAccountBalance(accountId, amount);

        dispenseCash(handle, amount);
    }

    private DeviceHandle fetchDeviceHandle() throws DeviceNotFoundException {

        DeviceHandle handle = getHandle("DEV1");

        if (handle == DeviceHandle.INVALID) {
            throw new DeviceNotFoundException("ATM device not found");
        }

        return handle;
    }

    private DeviceRecord fetchDeviceRecord(DeviceHandle handle) {
        return retrieveDeviceRecord(handle);
    }

    private void validateDeviceStatus(DeviceRecord record) throws DeviceLockedException {

        if (record.getStatus() == DEVICE_SUSPENDED) {
            throw new DeviceLockedException("ATM device is suspended");
        }
    }

    private void validateNetworkConnection(DeviceRecord record) throws NetworkConnectionException {

        if (record.getWifiConnection() != WIFI_CONNECTED) {
            throw new NetworkConnectionException("ATM network connection failed");
        }
    }

    private void validateAccountBalance(String accountId, double amount) throws InsufficientFundsException {

        if (getBalance(accountId) < amount) {
            throw new InsufficientFundsException("Insufficient balance");
        }
    }

    private void dispenseCash(DeviceHandle handle, double amount) {
        System.out.println("Dispensing cash: " + amount);
    }
}
