Manage Common Parameters Sample Application
===========================================

This sample Python application shows how to get and set common parameters of
the XBee device. Common parameters are split in cached and non-cached
parameters. For that reason, the application refreshes the cached parameters
before reading and displaying them. It then configures, reads and displays
the value of non-cached parameters.

The application uses the specific setters and getters provided by the XBee
device object to configure and read the different parameters.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.

Run
---
1. The example is already configured, so all you need to do is to compile and
   launch the application.

2. When the application finishes the following message should be displayed:

       Cached parameters
       --------------------------------------------------
       64-bit address:   XXXXXXXXXXXXXXXX
       16-bit address:   00 00
       Node Identifier:  <gateway NI>
       Firmware version: 10 09
       Hardware version: XBEE3

       Non-Cached parameters
       --------------------------------------------------
       PAN ID:           00 00 00 00 00 00 01 23
       Dest address:     000000000000FFFF
       Power level:      Medium

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
