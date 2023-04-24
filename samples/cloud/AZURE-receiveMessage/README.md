AZURE Receive Message Sample Application
========================================

This sample Python application shows how to receive a message from the Azure Cloud.

Code is a copy of:
https://github.com/Azure/azure-iot-sdk-python/blob/master/azure-iot-device/samples/sync-samples/receive_message_x509.py

Requirements
------------
To run this example you will need:

* Network connectivity to Azure.
* System configured with the correct certificates installed on it.
* Environment variables pointing to required Azure information.

Setup
-----
1. Install/upload the Azure device certificate in your device.

2. Export/Setup the next environment variables as:
    - HOSTNAME=<azure-hub-name>
    - X509_CERT_FILE=<path_to_device_full_certificate>
    - DEVICE_ID=<Azure_device_id>
    - X509_KEY_FILE=<path_to_device_private_key>
    - PASS_PHRASE=<Passphrase of your Azure DPS service>

Run
---
1. Run the application.

Supported platforms
-------------------
* AnywhereUSBPlus
* ConnectEZMini
* ConnectEZ2
* ConnectEZ4
* ConnectEZ8
* ConnectEZ1632
* ConnectITMini
* ConnectIT4
* ConnectIT1648
* EX12
* EX15
* EX50
* IX10
* IX15
* IX20
* IX30
* LR54
* TX54
* TX64
* TX64Rail

License
-------
Copyright (c) 2020-2023, Digi International, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
