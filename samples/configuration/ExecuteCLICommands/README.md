Execute CLI Commands Sample Application
=======================================

This sample Python application shows how to use CLI API of the Cellular Routers
and XBee Gateways to execute CLI commands in the devices.

The example executes the command 'show system' to retrieve status and
statistical information about the device and then lists the content of its root
path.

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
   launch the **Execute CLI Commands** application in the Digi device.

2. The application reads the system information executing a CLI command. Verify
   the application displays the answer to that command, something similar to:
   
       SYSTEM INFORMATION (show system)
       ------------------------------------------------------------------------
       Model                    : Digi IX15      
        Serial Number            :                
        SKU                      : Not Available  
        Hostname                 : Digi IX15      
        MAC                      : 00:27:04:03:02:01
       
        Hardware Version         : Not Available  
        Firmware Version         : 20.7.186.0-eb5a603d45-dirty
        Alt. Firmware Version    : 20.7.186.0-eb5a603d45-dirty
        Bootloader Version       : 20.7.162.1-a07e5c581a-dirty
       
        Current Time             : Mon, 03 Aug 2020 15:50:16 +0000
        CPU                      : 16.8%          
        Uptime                   : 53 minutes, 27 seconds (3207s)

3. Finally, the application lists the content of the root path of the device by
   executing the `ls /` CLI command. The application should output the contents
   of the root path as follows:

       LIST ROOT (ls /)
       ------------------------------------------------------------------------
       drwxr-xr-x    2 root     root          4163 Aug  3 11:13 bin
       drwxr-xr-x   10 root     root          3120 Aug  3 14:57 dev
       drwxr-xr-x   29 root     root          1291 Aug  3 11:13 etc
       drwxr-xr-x    3 root     root            28 Aug  3 11:01 home
       drwxr-xr-x   18 root     root          4672 Aug  3 11:14 lib
       drwxr-xr-x    5 root     root           125 Aug  3 11:13 libexec
       drwxr-xr-x    3 root     root           296 Aug  3 11:39 opt
       drwxr-xr-x    2 root     root             3 Aug  3 11:02 overlay
       dr-xr-xr-x  119 root     root             0 Aug  3 14:56 proc
       lrwxrwxrwx    1 root     root             8 Aug  3 11:12 run -> /var/run
       drwxr-xr-x    2 root     root          1473 Aug  3 11:13 sbin
       dr-xr-xr-x   12 root     root             0 Aug  3 14:56 sys
       drwxrwxrwt    3 root     root           100 Aug  3 15:46 tmp
       drwxr-xr-x    9 root     root           115 Aug  3 11:01 usr
       drwxrwxrwt    9 root     root           180 Aug  3 14:57 var

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
