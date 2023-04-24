Receive SMS Sample Application
==============================

This sample Python application shows how SMS messages are received by a
Cellular Router using a callback executed every time a new SMS is received.

The application prints the phone that sent the message and the text of the
SMS itself.

Requirements
------------
To run this example you will need:

* A Cellular Router device with the micro SIM card inserted.
* A mobile phone to send the SMS message.

Setup
-----
1. Make sure the Cellular Router is associated to the cellular network so that
   the device is able to receive SMS from other cellular devices. To do so,
   open the dashboard of your device and go to **Status > Modems**. There,
   verify that the **State** parameter within the **Status** group is
   **Connected**.

2. Get the phone number of the SIM card so you can send the SMS from your
   smartphone. To do so, open the dashboard of your device and go to **Status >
   Modems**. Once there, write down the phone number you will find in the
   **Phone number** parameter within the **SIM** group.

Run
---
1. The example is already configured, so all you need to do is to build and
   launch the **Receive SMS** application in the Digi device. The script waits
   for the reception of SMS messages and prints the following line:
   
       - Waiting for SMS messages...
       
2. Whenever an SMS is received, the application prints the following text:

       - Received SMS message from 'XXXXXXXXXX' >> '<TEXT>'
   
   where:
   
   - `XXXXXXXXXX` is the phone number that sent the SMS.
   - `<TEXT>` is the text contained in the SMS.

3. Press any key to halt the application execution.

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
