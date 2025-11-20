Receive Data Sample Application
===============================

This sample Python application shows how to receive RS485 data using a serial
port.

The application receives data from the configured serial port and prints it
decoded in utf-8 format.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* Another device with an available serial port, for example a PC.
* A proper serial cable to connect the XBee Gateway serial port and the
  other port.
* Another instance of PyCharm with the **RS485 > Send Data** sample
  loaded (located in the *SERIAL* category).

Setup
-----
1. Configure the serial port of the XBee Gateway in 'Application' mode.
   From the WebUI go to 'System > Device Configuration > Serial'
   Set 'Application' in the 'Serial mode' combo of the port.

2. Connect the XBee Gateway serial port with the PC serial port using the
   serial cable.

3. Set the port and baud rate of the XBee Gateway in the sample file.

4. Set the port and baud rate of the PC in the sample file of **Send Data**.

Run
---
1. The example is already configured, so all you need to do is to build and run
   the project in the XBee Gateway.

2. Launch the **Send Data** sample in the PC.

3. Data received by the XBee Gateway is printed out in the console

       Hello from RS485 TX side

Supported platforms
-------------------
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
