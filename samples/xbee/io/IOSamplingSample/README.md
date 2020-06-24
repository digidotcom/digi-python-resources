IO Sampling Sample Application
==============================

This sample Python application shows how to configure a remote device to send
automatic IO samples and how to read them from the local module.

The application configures two IO lines of the remote XBee device: one as
digital input (button) and the other as ADC, and enables periodic sampling
and change detection. The device sends a sample every five seconds containing
the values of the two monitored lines. It sends another sample every time the
button is pressed or released, which only contains the value of this digital
line.

Then, the application registers a listener in the local device to receive and
handle all IO samples sent by the remote XBee module.

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

2. Verify that the samples are received and printed in the output console
   every 5 seconds. These samples should contain the values of the two lines
   that are monitored.

        New sample received from 0013A20040XXXXXX - {[IOLine.DIO1_AD1: IOValue.HIGH], [IOLine.DIO3_AD3: IOValue.HIGH], [IOLine.DIO2_AD2: 1023]}

   where:

   - `0013A20040XXXXXX`is the 64-bit address of the remote Zigbee device
     that sent the data frame.

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
