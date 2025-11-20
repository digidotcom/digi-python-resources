Handle SCI Requests Sample Application
======================================

This sample Python application shows how to use the Cellular Router or XBee
Gateway to receive and handle requests from Digi Remote Manager cloud.

The example registers a callback to process device requests with a specific
target ID coming from the cloud and prints their value.

Requirements
------------
To run this example you will need:

* A Digi Cellular router or XBee gateway device.
* A Digi Remote Manager account with your Digi device added to it.
  Go to https://myaccount.digi.com/ to create it if you do not have one.

Setup
-----
1. Make sure that the Digi Device is connected to Internet and it is registered
   in your Digi Remote Manager account.

Run
---
1. The example is already configured, so all you need to do is to build and
   launch the **Handle SCI Requests** application in the Digi device. The
   application prints the following message:
   
       - Waiting for Digi Remote Manager requests...

2. In your Digi Remote Manager account, go to **Documentation > API Explorer**.
   Then, select the example **Examples > SCI > Data Service > Send Request** to
   generate the URL and template of the send request. Complete the request as
   follows:

       <sci_request version="1.0">
         <data_service>
           <targets>
             <device id="00000000-00000000-XXXXXXXX-XXXXXXXX"/>
           </targets>
           <requests>
             <device_request target_name="myTarget">
               Hello from Digi Remote Manager!
             </device_request>
           </requests>
         </data_service>
       </sci_request>

   where:

     - `00000000-00000000-XXXXXXXX-XXXXXXXX` is the device ID of your Cellular
       Router or  XBee Gateway device.
     - `myTarget` is the target name of the Digi Remote Manager requests
       handler you configured in the Python script. Both target names (the one
       from the Python script and the request one) must be the same. So, if
       you modified it in the script, update it in the request too.
     - `Hello from Digi Remote Manager!` is the content of the request.

3. Click the **Send** button to send the request to the device. 

4. Verify that a new line is printed out in the console with the following
   message:
   
       - Received request 'Hello from Digi Remote Manager!' for target 'myTarget'
   
   Verify also that the **Response** tab of the **API Explorer** displays a
   response similar to:
   
       <sci_reply version="1.0">
         <data_service>
           <device id="00000000-00000000-XXXXXXXX-XXXXXXXX">
             <requests>
               <device_request target_name="myTarget" status="0">OK</device_request>
             </requests>
           </device>
         </data_service>
       </sci_reply>
   
   where:
   
     - `00000000-00000000-XXXXXXXX-XXXXXXXX` is the device ID of your Cellular
       Router or  XBee Gateway device.
     - `myTarget` is the target name of the Digi Remote Manager requests
       handler you configured in the Python script.
     - `OK` is the answer to the request reported by the Python script.
     
5. Press any key to halt the application execution.

Supported platforms
-------------------
* AnywhereUSBPlus
* ConnectEZMini
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
