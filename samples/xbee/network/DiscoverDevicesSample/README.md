Discover Devices Sample Application
===================================

This sample Python application demonstrates how to obtain the XBee network
object from the XBee Gateway device and discover the remote XBee devices that
compose the network. The example adds a discovery listener, so the events
will be received by the callbacks provided by the listener object.

The remote XBee devices are printed out as soon as they are found during the
discovery.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* At least an extra Zigbee radio in API mode and its corresponding carrier
  board (XBIB-U-DEV or XBIB-C board).

Run
---
1. The example is already configured, so all you need to do is to compile and
   launch the application.

2. When the application finishes the following message should be displayed:

       Discovering remote XBee devices...
       Device discovered: 0013A20040XXXXXX - REMOTE
       Discovery process finished successfully.

   where:

   - `0013A20040XXXXXX` is the 64-bit address of the remote ZigBee device and
   `REMOTE` its Node Identifier.

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
