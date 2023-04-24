Digi Remote Manager Send Single Data Point
==========================================

This sample Python application shows how to send a single data point from your
XBee Gateway to Digi Remote Manager.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* A Digi Remote Manager account with your XBee Gateway added to it.
  Go to https://myaccount.digi.com/ to create it if you do not have one.

Setup
-----
Make sure the hardware is set up correctly:

1. Ensure that your gateway is connected to Digi Remote Manager.

Run
---
The example is already configured, so all you need to do is to compile and
launch the application. When executed, it starts uploading the temperature
of the XBee Gateway to your Digi Remote Manager account every 10 seconds
during a minute.

Follow these steps to verify the temperature is being uploaded to your Digi
Remote Manager account:

1. Log in your Digi Remote Manager account using your credentials:
   https://remotemanager.digi.com/login.do
2. Within the Digi Remote Manager platform, select the **Data Streams**
   option of the list at the left.
3. Look for the stream **single_temperature**.
4. Select the stream and verify the chart displays the temperature of the
   module as it is being sent.

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
Copyright (c) 2021-2023, Digi International, Inc.

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
