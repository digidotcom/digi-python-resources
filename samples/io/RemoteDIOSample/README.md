Remote DIO Sample Application
=============================

This sample Python application shows how to set and read XBee digital lines of
remote devices.

The application configures two IO lines of the XBee devices, one in the
remote device as a digital input (button) and the other in the local device
as a digital output (LED). Then, the application reads the status of the
input line periodically and updates the output to follow the input.

While the push button is pressed, the LED should be lighting.

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

2. Ensure that the module is in API mode and on the same network as the
   gateway.

3. The final step is to configure the IO lines in the example. Depending
   on the carrier board you are using you may need to change a couple of
   lines in the example code:
     - XBIB-U-DEV board:
         * The example is already configured to use this carrier board.
           The input line is configured to use the SW5 user button of the
           board and the output line is connected to the DS4 user LED. No
           further changes are necessary.

     - XBee Development Board:
         * If you are using the XBee Development Board, update the IOLINE_IN
           constant accordingly.

     NOTE: It is recommended to verify the capabilities of the pins used
           in the example in the product manual of your XBee Device to
           ensure that everything is configured correctly.

Run
---
1. The example is already configured, so all you need to do is to compile and
   launch the application.

2. Press the button corresponding to the digital input line in the remote
   XBee device. In the XBIB boards it is the DIO3.

3. Verify that the status of the LED corresponding to the digital output
   line in the local XBee device changes. In the XBIB boards it is the DIO4.

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
