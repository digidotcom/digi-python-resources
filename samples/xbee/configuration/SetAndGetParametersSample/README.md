Set And Get Parameters Sample Application
=========================================

This sample Python application shows how to set and get parameters of a local
XBee Gateway device. This method is intended to be used when you need to set or
get the value of a parameter that does not have its own getter and setter
within the XBee Gateway device object.

The application sets the value of four parameters with different value types:
string, byte array and integer. Then it reads them from the device to verify
that the read values are the same as the values that were set.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.

Run
---
1. The example is already configured, so all you need to do is to compile and
   launch the application.

2. When the application finishes the following message should be displayed:

       Node ID:                     Yoda
       PAN ID:                      00 00 00 00 00 00 12 34
       Destination address high:    00 00 00 00
       Destination address low:     00 00 FF FF

       "All parameters were set correctly!"

Supported platforms
-------------------
* IX15

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
