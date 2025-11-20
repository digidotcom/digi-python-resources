AWS Basic Public Subscribe Sample Application
=============================================

This sample Python application demonstrates a simple MQTT publish/subscribe
using AWS IoT. It first subscribes to a topic and registers a callback to print
new messages and then publishes to the same topic in a loop. New messages are
printed upon receipt, indicating the callback function has been called.

Code is base on:
https://github.com/aws/aws-iot-device-sdk-python/blob/master/samples/basicPubSub/basicPubSub.py

Requirements
------------
To run this example you will need:

* Network connectivity to AWS.
* System configured with the correct certificates installed on it.

Setup
-----
1. Install the Amazon certificate in your device.
    curl https://www.amazontrust.com/repository/AmazonRootCA1.pem > /opt/AWS-root-CA.crt

2. Install/upload the AWS device certificate in your device.

Run
---
1. Run this application with the next arguments:

    -e  <account-specific-prefix.iot.aws-region.amazonaws.com> -r /opt/AWS-root-CA.crt  -k device.key  -c device-signed+CA.crt

    where:

    - `-e` is your AWS iot-endpoiont with format account-specific-prefix.iot.aws-region.amazonaws.com
    - `AWS-root-CA.crt` is the amazon certificate
    - `device.key` is the path to your private device key
    - `device-signed+CA.crt` is the path to your device signed plus CA signed key

Supported platforms
-------------------
* AnywhereUSBPlus
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
Copyright (c) 2020-2023, Digi International, Inc.

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
