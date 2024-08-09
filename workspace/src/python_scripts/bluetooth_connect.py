#ps5_address = "D0:BC:C1:BB:A8:10"

import asyncio
from bleak import BleakScanner, BleakClient

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

    # Connect to a specific device
    address = "D0:BC:C1:BB:A8:10"  # Replace with your device's address
    async with BleakClient(address) as client:
        # Interact with the device
        # For example, read a characteristic:
        # value = await client.read_gatt_char("CHARACTERISTIC_UUID")
        print("Connected to device")

asyncio.run(main())