Upload Device Name Sample Application
=====================================

This sample Python application shows how to upload a custom name for your
device to Digi Remote Manager.

The example changes the name of the Digi device in Digi Remote Manager with
the value of the `NEW_DEVICE_NAME` constant.

You should take this considerations into account when changing the name of
your device in Digi Remote Manager:

- If the name is being used by to another device in your Remote Manager
  account, the name will be removed from the previous device and added to the
  new device.
- If Remote Manager is configured to apply a profile to a device based on the
  device name, changing the name of the device may cause Remote Manager to
  automatically push a profile onto the device.

Requirements
------------
To run this example you will need:

* A Digi Cellular router or XBee gateway device.
* A Digi Remote Manager account with your Digi device added to it.
  Go to https://myaccount.digi.com/ to create it if you do not have one.

Setup
-----
1. Make sure that the Digi Device is connected to Internet and it is registered
   in your Digi Remote Manager account.

2. Make sure your account allows remote name updates in Digi Remote Manager.
   To enable such feature, access Remote Manager and go to **Documentation >
   API Explorer**. There, configure the following elements:
   
   - **Path**: `/ws/v1/settings/inventory/AllowDeviceToSetOwnNameEnabled`
   - **HTTP Method**: `PUT`
   - **HTTP Message**:
   
         {
             "name" : "AllowDeviceToSetOwnNameEnabled",
             "value" : "true"
         }
   
   Then, click **Send**. 

Run
---
1. The example is already configured, so all you need to do is to build and
   launch the **Upload Device Name** application in the Digi device. The
   application just updates the name of the device in Digi Remote Manager with
   the one configured in the `NEW_DEVICE_NAME` constant. To indicate so, it
   displays the following message in the console log:
   
       - Updating the device name with 'MY-DEVICE' to Digi Remote Manager

2. In your Digi Remote Manager account, go to **Device Management** tab and
   click the **Refresh** button. Then, verify that the **Device Name** column
   of the devices table displays the new name for your Digi Device.

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
* Digi EX15/EX15W
* Digi EX50
* Digi IX10
* Digi IX15 XBee Gateway
* Digi IX20/IX20W
* Digi IX30
* Digi LR54/LR54W
* Digi TX54
* Digi TX64
* Digi TX64 Rail

License
-------
Copyright (c) 2023, Digi International, Inc.

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
