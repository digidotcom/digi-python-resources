Wake up from RTC Sample Application
===================================

This sample Python application shows how to configure the device to wake up
using an RTC alarm.

The application configures the RTC interface as a wake up source by setting a
specific date/time for the alarm; then the device goes to suspend. When the
configured RTC alarm triggers, the device wakes up.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.

Setup
-----
1. Set the desired RTC alarm date/time in the sample file.

Run
---
1. The example is already configured, so all you need to do is to build and run
   the project in the XBee Gateway.

2. As soon as the application is launched, the device will go to suspend.

3. When the configured RTC alarm triggers, the device wakes up.

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
