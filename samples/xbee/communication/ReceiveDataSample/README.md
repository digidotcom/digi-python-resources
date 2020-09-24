Receive Data Sample Application
===============================

This sample Python application shows how data packets are received from another
XBee device on the same network.

The application prints the data that was received to the standard output in
ASCII and hexadecimal formats after the sender address.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* At least an extra Zigbee radio in API mode and its corresponding carrier
  board (XBIB-U-DEV or XBIB-C board).
* The XCTU application (available at www.digi.com/xctu).

Setup
-----
1. Find the 64-bit address of the XBee Gateway's local module from the **XBee**
   section of the XBee Gateway UI. It is a 16 character string that follows
   the format 0013A20040XXXXXX and will be used later in the example. The
   application will display this address at the beginning of the execution.

2. Plug the Zigbee radio into the XBee adapter and connect it to your
   computer's USB or serial port.

3. Ensure that the module is in API mode and on the same network as the
   gateway.

Run
---
1. The example is already configured, so all you need to do is to compile and
   launch the application.

2. Then, you need to send a **Transmit Request** frame to the receiver (gateway)
   XBee module from another device on the network. Follow the steps below to
   do so:

     1. Launch the XCTU application.

     2. Add the sender (remote) Zigbee module to XCTU, specifying its port
        settings.

     3. Once the module is added, change to the **Consoles** working mode and
        open the serial connection.

     4. Create and add a frame using the **Frames Generator** tool with the
        following parameters:

            - Protocol:                               Select the protocol of your device.
            - Frame type:                             Select a Transmit Request frame.
            - Frame ID:                               01
            - 64-bit dest. address:                   Use the 64-bit address you copied before.
            - 16-bit dest. address (only if present): FF FE
            - Broadcast radius (only if present):     00
            - Options:                                00
            - RF data (ASCII):                        Hello XBee!

     5. Send this frame by selecting it and clicking the **Send selected Frame**
        button.

3. When the data frame is sent, verify that a line with the data frame and the
   data included in the **RF data** field is printed out in the console of the
   launched application:

       From 0013A20040XXXXXX >> Hello XBee!

   where:

   - `0013A20040XXXXXX` is the 64-bit address of the remote Zigbee device
     that sent the data frame.

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
