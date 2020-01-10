Remote ADC Sample Application
=============================

This sample Python application shows how to read XBee analog inputs of remote
XBee devices.

The application configures an IO line of the remote XBee device as ADC. Then,
it periodically reads its value and prints it in the output console.

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

3. The final step is to connect a voltage variable source to the pin
   configured as ADC in the remote XBee device (light sensor, temperature
   sensor, etc). For testing purposes we recommend using a potentiometer.
   Depending on the carrier board you are using you will need to follow a
   different set of instructions to connect it:
     - XBIB-U-DEV board:
         * Isolate the pin configured as ADC so it does not use the
           functionality provided by the board.
         * Connect the potentiometer to VCC, to the pin configured as ADC
           and to GND. Something similar to this:

               O   VCC
               |
               <
               >___ XBee device pin (ADC)
               >
               <
              _|_
               -   GND

         * If you prefer not to isolate the pin of the board and not to use
           a potentiometer, you can still test the example. The IO line
           configured as ADC (DIO1/AD1) is connected to the SW3 user button
           of the XBIB-U-DEV board, so the analog value will change from
           nothing to all depending on the status of the button.

     - XBee Development Board:
         * Connect a voltage to VRef pin of the device (you can take it
           from the Vcc pin).
         * Configure the micro-switch of AD1 line to "Potentiometer", this
           way the DIO1/AD1 line of the device will be connected to the
           board's potentiometer

     NOTE: It is recommended to verify the capabilities of the pins used
           in the example as well as the electrical characteristics in the
           product manual of your XBee Device to ensure that everything is
           configured correctly.

Run
---
1. The example is already configured, so all you need to do is to compile and
   launch the application.

2. Verify that the samples are received and printed in the output console.

3. Rotate the potentiometer and verify that the value displayed in the output
   console is changing.

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
