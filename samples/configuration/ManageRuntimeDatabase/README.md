Manage Runtime Database Sample Application
==========================================

This sample Python application shows how to access and modify the device
runtime database using the `runt` Python submodule.

The example lists all the runtime database available elements. Then, it gets
and prints all the system (`system`) sub-elements and the value of the system
MAC (`system.mac`) element. Finally it shows how to create a new variable in
the runtime database and reads its value.

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
   launch the **Manage Runtime Database** application in the Digi device.

2. The first thing the application does when it is started is to get and print
   all the available elements of the runtime database:
   
       Runtime database elements:
        - advanced
        - cc_watchdog
        - drm
        - firmware
        - manufacture
        - metrics
        - mm
        - my_new_var
        - network
        - serial
        - system
        - xbee
        
3. Then, it gets and prints all the `system` sub-elements:
   
       System (system) elements:
        - boot_count
        - cpu
        - cpu_temp
        - cpu_usage
        - disk
        - load_avg
        - local_time
        - mac
        - model
        - ram
        - serial
        - uptime

4. The next operation the application does is to read and print the value of
   the system MAC (`system.mac`) element:

       System MAC (system.mac) value: 002704030201

5. Finally, the application adds a new variable (`my_new_var`) to the runtime
   database and prints the value it was assigned when it was added:
   
       Generating new variable 'my_new_var'
        - Value read from 'my_new_var' variable: 110777

Supported platforms
-------------------
* AnywhereUSBPlus
* ConnectEZMini
* ConnectEZ2
* ConnectEZ4
* ConnectEZ8
* ConnectEZ1632
* ConnectITMini
* ConnectIT4
* ConnectIT1648
* EX12
* EX15
* EX50
* IX10
* IX15
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
