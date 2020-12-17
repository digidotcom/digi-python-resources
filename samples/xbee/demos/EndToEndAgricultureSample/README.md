End to End Agriculture IoT Sample Application
=============================================

This example is part of the Digi's End-to-End Agriculture IoT demo. It
demonstrates how to use the XBee Gateway and the XBee 3 modules to exchange
data, communicate with Digi Remote Manager and use the BLE interface to talk to
mobile apps applied to the agriculture vertical.

The XBee Gateway this example runs in corresponds to an irrigation controller
that manages several irrigation stations within an installation. In addition, it
is connected to the following sensors but, for demonstration purposes, they are
emulated:

* Weather station:
  * Rain gauge.
  * Anemometer.
  * Pyranometer.
* Water tank:
  * Water level sensor.
  * Electronic valve.

The example performs the following actions:

* Listen for BLE connections to execute the provisioning process (initial
  configuration of the irrigation controller properties).
* Listen for data coming from the irrigation stations and upload it to Digi
  Remote Manager.
* Read the values of the sensors and upload them to Digi Remote Manager
  periodically.
* Generate the corresponding irrigation commands based on the configured
  schedule, tank level and moisture.
* Listen for requests coming from Digi Remote Manager and distribute them to
  the corresponding irrigation stations.

Read the [demo documentation][doc] for more information.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* At least one XBee 3 radio module with MicroPython support running the
  corresponding MicroPython application of the demo and its corresponding
  carrier board (XBIB-C board).
* A smartphone running the corresponding mobile app of the demo.
* A Digi Remote Manager account. Go to https://myaccount.digi.com/ to create it
  if you do not have one.

Setup
-----
Make sure the hardware is set up correctly:

1. Plug the Ethernet, antenna and power cables to the XBee Gateway.

Run
---
The example is already configured, so all you need to do is build and launch
the project. Then, read the demo documentation for more information about how
to test the demo.

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


[doc]: https://www.digi.com/resources/documentation/digidocs/90002422
