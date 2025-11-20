Send Data Asynchronously Sample Application
===========================================

This sample Python application shows how to send data asynchronously to a
remote device on the same network. Transmitting data asynchronously means the
execution will not be blocked during the transmit request, but you will not be
able to determine if the data was sent successfully.

The application sends data asynchronously to a remote XBee device on the network
with a specific node identifier (name).

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

2. Configure the remote Zigbee device with the Node Identifier used by the
   example to communicate with it and to receive data in application layer
   (explicit) format. To do so follow these steps:

     1. Launch the XCTU application.

     2. Add the remote Zigbee module to XCTU, specifying its port settings.

     3. Once the module is added, open the **Configuration** working mode,
        look for the **NI** setting and configure it with **REMOTE**.

        Notice that by default the 'NI' setting has a blank space
        configured, make sure that there is not a blank space before the
        **REMOTE* text.

3. Ensure that the module is in API mode and on the same network as the
   gateway.

Run
---
1. Setup XCTU to see the data received by the remote Zigbee device format.
   Follow these steps to do so:

     1. Launch the XCTU application.

     2. Add the remote ZigBee module to XCTU, specifying its port settings.

     3. Switch to the **Consoles** working mode and open the serial connection
        so you can see the data when it is received.

2. Run the sample application. Data is sent to the configured remote ZigBee
   device whose Node Identifier is **REMOTE**. When that happens, a line with
   the result of the operation is printed to the standard output:

       Sending data asynchronously to 0013A20040XXXXXX >> Hello XBee!...
       Success

   where:

   - `0013A20040XXXXXX` is the 64-bit address of the remote ZigBee device
     whose Node Identifier is **REMOTE**.

3. Verify that in the XCTU console a new **Receive Packet** frame has been
   received by the remote Zigbee device. Select it and review the details,
   some of the details will be similar to:

       - Start delimiter:         7E
       - Length:                  00 17
       - Frame type:              90
       - 64-bit source address:   The XBee sender's 64-bit address.
       - 16-bit source address:   The XBee sender's 16-bit address.
       - Receive options:         01
       - RF data/Received data:   48 65 6C 6C 6F 20 58 42 65 65 21
                                  Hello XBee!

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
