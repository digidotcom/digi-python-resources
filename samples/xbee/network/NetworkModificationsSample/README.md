Network Modifications Sample Application
========================================

This sample Python application demonstrates how to listen to network
modification events. The example adds a modifications network callback,
so modifications events are received and printed out.

A network is modified when:
* a new node is added by discovering, manually, or because data is received
from it
* an existing node is removed from the network
* an existing node is updated with new information
* it is fully cleared

Requirements
------------
To run this example you will need:

* An XBee Gateway device.
* At least an extra Zigbee radio in API mode and its corresponding carrier
  board (XBIB-U-DEV or XBIB-C board).

Run
---
1. The example is already configured, so all you need to do is to compile and
   launch the application.

2. When the application finishes the following message should be displayed:
    1. It performs a device discovery in the network.
       For each discovered device the output console displays the following
       message:

           * Discover remote XBee devices...
           >>>> Network event:
                  Type: XBee added to the network (0)
                  Reason: Discovered XBee (0)
                  Node:
                     XXXXXXXXXXXXXXXX - <NODE_ID>

       where:

       - `0013A20040XXXXXX` is the 64-bit address of the remote ZigBee device and
       `REMOTE` its Node Identifier.

    2. Then, it manually adds a new node to the network cache.

           * Manually add a new remote XBee device...
           Current network nodes:
                >>>> Network event:
                   Type: XBee added to the network (0)
                   Reason: Manual modification (3)
                   Node:
                      1234567890ABCDEF - manually_added

    3. It manually adds the same node but with a different node identifier.

           * Update the last added remote XBee device...
           Current network nodes:
               >>>> Network event:
                  Type: XBee in the network updated (2)
                  Reason: Manual modification (3)
                  Node:
                     1234567890ABCDEF - updated_node

    4. Then, it removes this node from the network cache.

           * Manually remove a remote XBee device...
               Current network nodes:
                   >>>> Network event:
                      Type: XBee removed from the network (1)
                      Reason: Manual modification (3)
                      Node:
                         1234567890ABCDEF - updated_node

    5. Finally, it clears the network.

           * Clear network...
             Current network nodes:
                 >>>> Network event:
                    Type: Network cleared (3)
                    Reason: Manual modification (3)

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
