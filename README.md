Python Resources for Digi Devices
=================================

This project contains modules and sample code for use on Digi devices with
Python support.

The repository is used by the **Digi Python PyCharm Plugin** to get the
available samples, libraries platforms and stubs and facilitate the process of
creating and launching Python applications in Digi devices. This means that you
don't need to clone it unless you want to contribute with new content as the
PyCharm plugin will handle all necessary resources automatically.

We don't recommend you to do so, but you can still use the content of this
repository to create Python applications by your own (without using the **Digi
Python PyCharm Plugin**). In any case, you will find information on how to get
started with Python in the [Applications][doc] section of your device
documentation.

[Digi International][Digi] manages the project on GitHub as
[digi-python-resources][digi-python-resources].


Requirements
------------

Modules and samples within the repository can be executed only in Digi devices
with Python support. This is the list of current compatible devices:

* IX15


Organization
------------

The repository is structured in the following folders:

* **categories** - This folder contains the definition and images for the Digi
  categories in which the different products supporting Python are organized.
  This information is used by the **Digi Python PyCharm Plugin** to filter the
  supported platforms.
* **lib** - The `lib/` directory contains Python modules that extend the
  standard API of your device. You can either import these libraries in your
  project using the **Digi Python PyCharm Plugin** or copy them manually inside
  your project structure.
* **platforms** - This folder contains the definition and images for the
  Digi products supporting Python. This information is used by the **Digi
  Python PyCharm Plugin** to list the supported platforms.
* **samples** - Files in the `samples/` directory are organized by feature.
  For example, `network` contains samples related to XBee networks and
  `configuration` contains samples demonstrating how to configure XBee
  devices.
* **typehints** - This folder contains the API definitions of the Python
  modules available in the Digi devices. These definitions are used by the
  **Digi Python PyCharm Plugin** for syntax checking, code completion and
  refactoring.


Usage
-----

For information on how to get started with Python in Digi products, see the
[Applications][doc] section of your device documentation.


How to Contribute
-----------------
The contributing guidelines are in the [CONTRIBUTING.md](CONTRIBUTING.md)
document.


License
-------

This software is open-source software. Copyright Digi International, 2020.

Samples within `samples/` folder, stub files in `typehints/` folder and most of
the source code in the `lib/` directory is covered by the
[MIT License](LICENSE.txt). Individual library files may contain alternate
licensing, depending on their origin.


[Digi]: http://www.digi.com
[digi-python-resources]: https://github.com/digidotcom/digi-python-resources
[doc]:https://www.digi.com/resources/documentation/digidocs/90002291/default.htm#containers/applications-cont.htm
