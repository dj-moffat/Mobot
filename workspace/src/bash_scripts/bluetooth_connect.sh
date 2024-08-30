#!/bin/bash

DEVICE_MAC="D0:BC:C1:BB:A8:10"

while true; do
    if ! bluetoothctl info $DEVICE_MAC | grep -q "Connected: yes"; then
        bluetoothctl connect $DEVICE_MAC
        sleep 10
    fi
done