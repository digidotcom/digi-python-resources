Send Bluetooth Data Sample Application
======================================

This sample Python application shows how to send data to the Bluetooth
interface of the XBee Gateway.

The application sends 10 messages to the Bluetooth Low Energy interface

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* An Android or iOS device with the Digi XBee Mobile application installed
  (available at Google Play and App Store).

Setup
-----
1. Enable the XBee Bluetooth interface of the XBee Gateway. To do so:
   
   1. Open the dashboard page of the device and go to 'System > Device
      Configuration'.
   2. Find and expand the 'XBee' configuration group.
   3. Enable the 'Bluetooth' interface.
   4. Configure the authentication password.
   5. Click 'Apply'.

Run
---
1. Set up the XBee Mobile app to see the data received. Follow these steps to
   do so:

     1. Launch the XBee Mobile application on your mobile device.

     2. Wait until your XBee device is discovered and connect to it with the
        password you configured during the setup.

     3. Open the Relay Console from the Options menu.

3. Then, launch the sample application. A total of 10 data messages are sent
   to the Bluetooth interface. When that happens, a line with the result of
   each operation is printed to the standard output:

       Sending data to Bluetooth interface >> 'Hello from the XBee Gateway (#1)'... Success
       Sending data to Bluetooth interface >> 'Hello from the XBee Gateway (#2)'... Success
       Sending data to Bluetooth interface >> 'Hello from the XBee Gateway (#3)'... Success
       ...

4. Verify in the Relay Console of the XBee Mobile app that new frames have been
   received. Tap on one of them and then on the info button, the details will
   be similar to:

       - Time:                    Received time.
       - Relay interface          SERIAL.
       - Data:                    Hello from the XBee Gateway (#1)

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
