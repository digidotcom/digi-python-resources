Send Broadcast Explicit Data Sample Application
===============================================

This sample Python application shows how to send data in application layer
(explicit) format to all remote devices on the same network (broadcast) as
the local one. The application will block during the transmission request,
but you will be notified if there is any error during the process.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* At least an extra Zigbee radio in API mode and its corresponding carrier
  board (XBIB-U-DEV or XBIB-C board).
* The XCTU application (available at www.digi.com/xctu).

Setup
-----
1. Plug the Zigbee radio into the XBee adapter and connect it to your
   computer's USB or serial port.

2. Configure the remote Zigbee device to receive data in application layer
   (explicit) format. To do so follow these steps:

     1. Launch the XCTU application.

     2. Add the remote Zigbee module to XCTU, specifying its port settings.

     3. Once the module is added, open the **Configuration** working mode,
        look for the **AO** setting and configure it with **1**.

3. Ensure that the module is in API mode and on the same network as the
   gateway.

Run
---
1. Setup XCTU to see the data received by the gateway in explicit format, in
   this case it will be broadcast data. Follow these steps to do so:

     1. Launch the XCTU application.

     2. Add the remote ZigBee module to XCTU, specifying its port settings.

     3. Switch to the **Consoles** working mode and open the serial connection
        so you can see the data when it is received.

2. Run the sample application. Data in explicit format is sent to all the
   remote modules of the network.

3. Verify that in the XCTU console a new **Explicit Rx Indicator** frame has
   been received by the remote ZigBee device. Select it and review the details,
   some of the details will be similar to:

       - Start delimiter:         7E
       - Length:                  00 23
       - Frame type:              91
       - 64-bit source address:   The XBee sender's 64-bit address.
       - 16-bit source address:   The XBee sender's 16-bit address.
       - Source endpoint:         A0
       - Destination endpoint:    A1
       - Cluster ID:              15 54
       - Profile ID:              12 34
       - Receive options:         02
       - RF data/Received data:   48 65 6C 6C 6F 20 58 42 65 65 20 57 6F 72 6C 64 21
                                  Hello XBee World!

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
