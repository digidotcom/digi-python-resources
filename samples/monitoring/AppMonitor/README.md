Application Monitor Sample Application
======================================

This sample Python application shows how to use the application monitor daemon
API.

The sample registers the application in the application monitor daemon and
starts refreshing it. After 5 loops, the application stops refreshing and waits
to be killed by the application monitor daemon.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.

Setup
-----
No special setup is required.

Run
---
1. The example is already configured, so all you need to do is to build and run
   the project in the XBee Gateway.

2. Upon start, the application registers to the application monitor daemon and 
   starts refreshing it.

3. After 5 refresh loops, the application stops refreshing and waits to be
   killed by the application monitor daemon.

Supported platforms
-------------------
* IX15

License
-------
Copyright (c) 2022, Digi International, Inc.

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
