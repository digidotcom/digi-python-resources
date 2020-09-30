Receive Bluetooth Data Sample Application
=========================================

This sample Python application shows how to receive and process data coming
from the Bluetooth interface of the XBee Gateway.

The application registers a callback to be notified when new data coming from
Bluetooth is received and prints it to the standard output.

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
1. The example is already configured, so all you need to do is to compile and
   launch the application.

2. Then, you need to send a User Data Relay message from the XBee Mobile
   application to the XBee Gateway. Follow the steps below to do so:

     1. Launch the XBee Mobile application on your mobile device.

     2. Wait until your XBee device is discovered and connect to it with the
        password you configured during the setup.

     3. Open the Relay Console from the Options menu.

     5. Tap on the Add (+) button to create a new frame. Select 'SERIAL' as
        Relay interface and enter 'Hello XBee Gateway!' as data. Then, tap on
        'Add'.

     6. Send this frame by selecting it and taping on 'Send selected frame'.

3. When the User Data Relay frame is sent, verify that a line with the data is
   printed out in the console of the launched application:

       Data received from Bluetooth >> 'Hello XBee Gateway!'

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
