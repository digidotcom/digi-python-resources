Wi-SUN Get Started Sample Application
=====================================

This example is part of the Digi's Wi-SUN Get Started. It demonstrates
how to use the XBee Hive Wi-SUN and the XBee Wi-SUN modules to exchange
data using the socket IPv6 API.

This application is executed in the XBee Hive Wi-SUN and performs the
following actions:
  * Allows the user to input messages to send to the target XBee.
  * Listens for incoming IPv6 messages from the XBee network.

Read the [demo documentation][doc] for more information.
  

Requirements
------------

To run this example you need:

* An XBee Hive Wi-SUN device.
* An XBee Wi-SUN radio module running the corresponding MicroPython 
  application of the Get Started and its corresponding carrier board
  (XBIB-C board).
* XBee Studio v1.3.0 or higher (available at www.digi.com/digi-xbee-studio)


Setup
-----

1. Ensure the XBee Wi-SUN module is in the same network as the Digi XBee Hive Wi-SUN device.

Run
---

The example expects the IPv6 address of the remote XBee device as a parameter to
launch. To obtain that value:

1. Launch the XBee Studio application.
2. Plug the remote XBee device to the PC. XBee Studio automatically discovers it.
3. Open the device tab associated to the XBee module by clicking on it.
4. Click **Settings** in the left sidebar to open the settings page. This reads
   all the settings automatically.
5. Search the **MY** setting. This is the value you have to pass as parameter
   to the Python application of the Digi XBee Hive Wi-SUN device.

Ensure to pass the XBee Device's IPv6 address as parameter to the example application. To do so from PyCharm:

1. Click on the **Run/debug Configurations** button in the toolbar of your IDE.
   It is a combo-box with the name of your project.
2. On the contextual menu that appears, click on **Edit Configurations**.
3. In the new window, there is a **Parameters** field. It allows to input the
   parameters of the application. Input **-a <destination_ipv6>** where
   <destination_ipv6> is the IPv6 address of the device that you copied 
   in the previous section.

At this point you only need to build and launch the project. Then, read the Get
started section of the documentation for more information about the exercise.

Supported platforms
-------------------

* Digi XBee Hive Wi-SUN - minimum firmware version: 25.8.138.60

License
-------

Copyright (c) 2025, Digi International, Inc.

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

[doc]: https://docs.digi.com/resources/documentation/digidocs/rf-docs/wisun/wisun-gs_c.html