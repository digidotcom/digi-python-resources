Send Data Sample Application
============================

This sample Python application shows how to send RS232 data using a serial
port.

The application sends data in utf-8 format through the configured serial port.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* Another device with an available serial port, for example a PC.
* A proper serial cable to connect the XBee Gateway serial port and the
  other port.
* Another instance of PyCharm with the **RS232 > Receive Data** sample
  loaded (located in the *SERIAL* category).

Setup
-----
1. Configure the serial port of the XBee Gateway in 'Application' mode.
   From the WebUI go to 'System > Device Configuration > Serial'
   Set 'Application' in the 'Serial mode' combo of the port.
   
2. Connect the XBee Gateway serial port with the PC serial port using the
   serial cable.

3. Set the port and baud rate of the XBee Gateway in the sample file.

4. Set the port and baud rate of the PC in the sample file of **Receive Data**.

Run
---
1. Launch the **Receive Data** sample in the PC.

2. The example is already configured, so all you need to do is to build and run
   the project in the XBee Gateway.

3. Data sent by the XBee Gateway is received in the PC and printed out in the
   console

       Hello from RS232 TX side

Supported platforms
-------------------
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
