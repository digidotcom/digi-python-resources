Send SMS Sample Application
===========================

This sample Python application shows how to send an SMS message from the
Cellular Router.

The application sends an SMS message to a mobile phone and prints the result
of the operation.

Requirements
------------
To run this example you will need:

* A Cellular Router device with the micro SIM card inserted.
* A mobile phone to receive the SMS message.

Setup
-----
1. Make sure the Cellular Router is associated to the cellular network so that
   the device is able to send SMS to other cellular devices. To do so, open the
   dashboard of your device and go to **Status > Modems**. There, verify that
   the **State** parameter within the **Status** group is **Connected**.

2. Set the value of **DEST** and **MESSAGE** constants in the Python file of
   **Send SMS**.

Run
---
1. The example is already configured, so all you need to do is to build and
   launch the **Send SMS** application in the Digi device. The script tries to
   send the SMS as soon as it is executed and prints the following line in the
   console:
   
       - Sending SMS to 'XXXXXXXXXX' >> '<TEXT>'...
   
   where:
   
   - `XXXXXXXXXX` is the phone number of the destination device.
   - `<TEXT>` is the text contained in the SMS.

2. Now, wait for the SMS reception in your mobile phone. When you receive it,
   the application displays the following text:
   
        - SMS sent successfully!

Supported platforms
-------------------
* Digi AnywhereUSB 2/8/24
* Digi Connect EZ Mini
* Digi Connect EZ 2
* Digi Connect EZ 4
* Digi Connect EZ 8
* Digi Connect EZ 16/32
* Digi Connect IT Mini
* Digi Connect IT 4
* Digi Connect IT 16/48
* Digi EX12
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
