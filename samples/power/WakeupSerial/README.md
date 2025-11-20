Wake up from serial Sample Application
======================================

This sample Python application shows how to configure the device to wake up
when some data is received in the serial port.

The application configures the serial port as a wake up source, opens the
serial port and then goes to suspend. When some data is received, the device
wakes up.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* Another device with an available serial port, for example a PC.
* A proper serial cable to connect the XBee Gateway serial port and the
  other port.

Setup
-----
1. Configure the serial port of the XBee Gateway in 'Application' mode.
   From the WebUI go to 'System > Device Configuration > Serial'
   Set 'Application' in the 'Serial mode' combo of the port.

2. Connect the XBee Gateway serial port with the PC serial port using the
   serial cable.

3. Set the port and baud rate of the XBee Gateway in the sample file.

4. Configure a Serial connection in the PC with the XBee Gateway using a
   terminal application such as TeraTerm and these settings:
       - Baudrate: The one specified before, 9600 by default.
       - Data Bits: 8
       - Stop Bits: 1
       - Parity: None
       - Flow Control: None

Run
---
1. The example is already configured, so all you need to do is to build and run
   the project in the XBee Gateway.

2. As soon as the application is launched, the device will go to suspend.

3. Send some data from the PC to the XBee Gateway using the configured serial
   console.

4. The XBee Gateway wakes up.

Supported platforms
-------------------
* Digi IX15 XBee Gateway

License
-------
Copyright (c) 2020, Digi International, Inc.

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
