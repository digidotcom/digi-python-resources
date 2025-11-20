Configure Device Sample Application
===================================

This sample Python application shows how to access and modify the configuration
of Cellular Routers and XBee Gateways through the `config` Python submodule.

The example lists all the configuration categories available in the device,
then, it reads and prints the network configuration interfaces and finally it
modifies the device description (`system.description`) parameter.

Requirements
------------
To run this example you will need:

* A Digi Cellular router or XBee gateway device.

Setup
-----
1. Ensure that the Digi Device is powered.

Run
---
1. The example is already configured, so all you need to do is to build and
   launch the **Configure Device** application in the Digi device.

2. The first thing the application does when it is started is to enumerate all
   the available configuration categories of the device. It prints something
   similar to:
   
       All available categories:
        - action
        - actiond
        - auth
        - cloud
        - device
        - firewall
        - firmware
        - imx
        - monitoring
        - network
        - schema
        - serial
        - seriald
        - service
        - system
        - vpn
        - xbee
        - xbee-bluetooth
        
3. Then, it accesses the `network.interface` category and lists all the
   available configuration categories inside that one:
   
       Network interfaces category (network.interface):
        - defaultip
        - defaultlinklocal
        - eth
        - loopback
        - modem

4. Finally, the application modifies the `system.description` configuration
   parameter. It reads the old value, then it updates it to `This is the
   description of my device` and prints the result of the operation.
   
       Updating device description...
        - Old description: 
        - New description: This is the new description of my device

Supported platforms
-------------------
* Digi AnywhereUSB 2/8/24
* Digi Connect EZ Mini
* Digi Connect EZ 2
* Digi Connect EZ 4
* Digi Connect EZ 8
* Digi Connect EZ 16/32
* Digi Connect IT Mini
* Digi Connect IT 4
* Digi Connect IT 16/48
* Digi EX12
* Digi EX15/EX15W
* Digi EX50
* Digi IX10
* Digi IX15 XBee Gateway
* Digi IX20/IX20W
* Digi IX30
* Digi LR54/LR54W
* Digi TX54
* Digi TX64
* Digi TX64 Rail

License
-------
Copyright (c) 2023, Digi International, Inc.

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
