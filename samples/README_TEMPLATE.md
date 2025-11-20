<Sample title> Sample Application
======================================

> REQUIRED
> 
> Brief description of the sample.
> 
> Example:

This sample Python application demonstrates how to obtain the XBee network 
object from a local XBee device and discover the remote XBee devices that 
compose the network. The example adds a discovery listener, so the events 
will be received by the callbacks provided by the listener object.
  
The remote XBee devices are printed out as soon as they are found during the 
discovery.
  
NOTE: This example uses the generic XBee device (XBeeDevice) class, but it 
      can be applied to any other local XBee device class.

Requirements
------------

> REQUIRED
> 
> This section lists the hardware and software components needed to run the
> sample application. Computer and PyCharm components are omitted.
>
> Example: 

To run this example you need:
  
  * At least two XBee radios in API mode and their corresponding carrier 
    board (XBIB or equivalent). More than two radios are recommended.
  * The XCTU application (available at www.digi.com/xctu).

Setup
-----

> REQUIRED
> 
> Describe here all the steps needed to connect and configure the hardware
> needed by the sample as well as any software configuration or changes in
> the code required prior to run the sample.
>
> Example:

Make sure the hardware is set up correctly:

1. Plug the XBee radios into the XBee adapters and connect them to your
   computer's USB or serial ports.

2. Ensure that the modules are in API mode and on the same network.
   For further information on how to perform this task, read the 
   'Configuring Your XBee Modules' topic of the Getting Started guide.

3. Set the port and baud rate of the local XBee radio in the sample file.
   If you configured the modules in the previous step with the XCTU, you 
   will see the port number and baud rate in the 'Port' label of the device 
   on the left view.

Run
---

> REQUIRED
> 
> In this section you must describe the steps needed to launch the sample and
> verify it is working properly.
>
> Example:

First, build and launch the application. As soon as the application is 
executed, it will perform a device discovery in the network. To verify the 
application is working properly, check that the following happens:

  1) The output console states the following message:

       "Discovering remote XBee devices..."

  2) For each discovered device the output console should display the 
     following message: 

       "Device discovered: XXXXXXXXXXXXXXXX"

         - Where XXXXXXXXXXXXXXXX is the MAC address of the remote XBee 
           device.

  3) When the discovery process finishes the following message should be 
     displayed:

       "Discovery process finished successfully."

Required libraries
--------------------

> OPTIONAL
>
> This section is used by the **Digi Python PyCharm Plugin** to import the
> libraries required by the sample application once the sample is imported.
> The content of the section is a list with the ID of required libraries from
> the `lib` directory. ID must equal the name of the library folder.
> 
> You can remove this section if the sample does not require any library.
> 
> Example:

* tftp

Supported platforms
-------------------

> REQUIRED
> 
> This section contains a list with the ID of Digi products compatible with
> the sample. You can take the ID of the platforms from the
> [platforms definition file](../platforms/platforms.xml).
> 
> Example:
   
* Digi IX15 XBee Gateway

License
-------

> REQUIRED
> 
> Attach here the license of the sample. Samples offered by Digi are covered
> by the [MIT license](https://en.wikipedia.org/wiki/MIT_License), so we 
> recommend you to use the same one changing the year and copyright holders
> as needed. 
> 
> Example:

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
