Synchronous RTU Client Sample Application
=========================================

This sample Python application shows how to run a Modbus synchronous RTU client
using pymodbus.

Code is base on next example:
https://github.com/riptideio/pymodbus/tree/master/examples/common/synchronous_client.py

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* Another instance of PyCharm with the **Synchronous RTU Server** sample loaded
  (located in the *MODBUS* category).
* A Modbus serial network.

Setup
-----
1. Set the port and baud rate of the XBee Gateway in the sample file.

2. Set the port and baud rate in the sample file of **Synchronous RTU Server**.

3. Create a Modbus network.

Run
---
1. Launch the **Synchronous RTU Server** application in the corresponding device.

2. Run this client application in the XBee Gateway, it reads data from the
   device with id `UNIT` (by default, 0).

Supported platforms
-------------------
* IX14

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
