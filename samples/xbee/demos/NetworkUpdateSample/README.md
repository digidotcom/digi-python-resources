Network Update Sample Application
=================================

This sample Python application shows how to update the XBee profile of one or
several XBee devices of your network using Digi Remote Manager.

The example registers a callback to process device requests coming from Digi
Remote Manager to trigger the profile update tasks. The profiles to apply to
the different XBee devices in the network must be already stored in the XBee
Gateway.

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* At least one XBee 3 radio module and its corresponding carrier board (XBIB-C
  board).
* One or more XBee profiles to apply to the XBee nodes.
* A Digi Remote Manager account with your XBee Gateway added to it.
  Go to https://myaccount.digi.com/ to create it if you do not have one.

Setup
-----
1. Plug the XBee radios into the XBee adapters and connect them to your
   computer's USB or serial port.

2. Ensure that the modules are on the same network as the gateway.

3. Ensure that the XBee profiles are stored in the XBee Gateway.

Run
---
The example is already configured, so all you need to do is to build and run
the project.

The application includes some options that you can review adding `-h` when
executing:

    usage: main.py [-h] [-d] [-i] [--log-console]
                   [--log-level <D, I, W, E>]

    Update XBee modules from Digi Remote Manager

    optional arguments:
      -h, --help            show this help message and exit
      -d, --discover        Discover network before performing an update (default:
                            False)
      -i, --ignore-invalid-tasks
                            Ignore invalid tasks in received requests (default:
                            False)
      --log-console         Enable log to standard output (default: False)
      --log-level <D, I, W, E>
                            Log level: debug, info, warning, error (default: I)

By default:

   * It does not discover the network.
   * It does not process invalid requests.
   * It only logs to `/var/run/messages` and not to the console.
   * The log level is `INFO`.

To verify the application is working properly, check the following:

1. After start, the application prints this message:

       Waiting for incoming XBee profile update requests...

2. In your Digi Remote Manager account, go to **Documentation > API Explorer**.

3. From **Examples** drop-down list, select **SCI > Data Service > Send Request**.

4. Inside the **Request** text field, paste and complete the following request
   to trigger a remote XBee profile update task:

       <sci_request version="1.0">
         <data_service>
           <targets>
             <device id="00000000-00000000-XXXXXXXX-XXXXXXXX"/>
           </targets>
           <requests>
             <device_request target_name="xbee_network_update">
               {
                   "tasks": [
                       {
                           "target": {
                               "type": TARGET_TYPE,
                               "value": TARGET_VALUE
                           },
                           "profile": PROFILE,
                           "timeout": TIMEOUT_SECONDS
                       },
                       ... more tasks ...
                   ]
               }
             </device_request>
           </requests>
         </data_service>
       </sci_request>

   where:

     * `00000000-00000000-XXXXXXXX-XXXXXXXX` is the device ID of your XBee Gateway.

     * `TARGET_TYPE` is the type of XBee target to update. It can be one of the
       following:
       - `0`: To update a specific XBee.
       - `1`: To update XBee nodes with a specific role.
       - `2`: To update a group of XBee devices.

     * `TARGET_VALUE` is the value of the update target, and its content depends
       on the value of `TARGET_TYPE` as follows:
       - `TARGET_TYPE=0`, value must be the 64-bit address of the XBee to update.
       - `TARGET_TYPE=1`, value must be one of the following:
         - `0`: to update the coordinator of the network
         - `1`: to update all network routers
         - `2`: to update all network end devices
       - `TARGET_TYPE=2`, value must be a comma-separated list of XBee 64-bit
         addresses to update.

     * `PROFILE` is the name of the XBee profile (with or without `.xpro`
       extension) to apply to the update target.

     * `TIMEOUT_SECONDS` is the maximum number of seconds to wait for read
       operations while applying the profile. It is an optional field.
   
   You can add more update tasks replacing the `MORE_TASKS_HERE` field.

   If there are more than one task for a node, the first task is the only one
   performed.

   For example:

       <sci_request version="1.0">
         <data_service>
           <targets>
             <device id="00000000-00000000-XXXXXXXX-XXXXXXXX"/>
           </targets>
           <requests>
             <device_request target_name="xbee_network_update">
               {
                   "tasks": [
                       {
                           "target": {
                               "type": 0,
                               "value": "0123456789ABCDEF"
                           },
                           "profile": "0123456789ABCDEF-profile"
                       },
                       {
                           "target": {
                               "type": 1,
                               "value": 0
                           },
                           "profile": "coordinator-profile.xpro",
                           "timeout": 30
                       },
                       {
                           "target": {
                               "type": 2,
                               "value": "0000000000000001,0000000000000002,0000000000000003"
                           },
                           "profile": "my-group_profile",
                           "timeout": 40
                       }
                   ]
               }
             </device_request>
           </requests>
         </data_service>
       </sci_request>

   This requests define 3 tasks:
     1. Update node (`TARGET_TYPE=0`) with 64-bit address `0123456789ABCDEF`
        using profile `0123456789ABCDEF-profile.xpro` and default timeout.
     2. Update all coordinators (`TARGET_TYPE=1`, `TARGET_VALUE=0`) with profile
        `coordinator-profile.xpro` and timeout of 40s.
     3. Update nodes (`TARGET_TYPE=2`) with 64-bit addresses `0000000000000001`,
        `0000000000000002` and `0000000000000003` using profile
        `my-group_profile.xpro` and timeout of 40s.

5. Verify that a new line is printed out in the console with the following
   message:

       Device request received to update the following XBee targets:
           - <64-bit_address_1> to <PROFILE_1>
           - <64-bit_address_2> to <PROFILE_2>
           . . .
           - <64-bit_address_n> to <PROFILE_N>

   At that moment, the profile update of the specified XBee devices starts.

Supported platforms
-------------------
* IX15

License
-------
Copyright (c) 2021, Digi International, Inc.

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
