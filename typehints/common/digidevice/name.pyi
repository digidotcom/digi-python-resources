"""
API for uploading a device name to DRM.

This module can be used to upload a custom name for a given device to DRM:

    from digidevice import name

    name.upload("myname")

When this module is used to upload a device name to DRM the following issues
apply:
    * If the name is being used by to another device in your DRM account, the
      name will be removed from the previous device and added to the new device.
    * If DRM is configured to apply a profile to a device based on the device
      name, changing the name of the device may cause DRM to automatically push
      a profile onto the device.

Together, these two features allow you to swap one device for another by using
the name submodule to change the device name, while guaranteeing that the new
device will have the same configuration as the previous one.

Check help(name.upload) for more details and parameters.
"""
# Copyright 2020, Digi International Inc.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


class NameException(RuntimeError):
    """
    Exception generated when a name fails to upload. Its message contains any
    captured output from the command. In the case of a server produced error,
    the value comes from the server.
    """
    def __init__(self, msg: str) -> None:
        """
        Class constructor. Instantiates a new ``NameException`` object
        with the provided parameters.

        :param msg: The message containing any captured output from the command.
            In the case of a server produced error, the value comes from the
            server.
        """
        ...


def upload(name: str, timeout: int=None) -> None:
    """
    Uploads a name to DRM. Because the name is sent to the server and
    communication can fail at any time, it's possible for this request to fail,
    but the name to still be successfully uploaded.

    Usage::

        name.upload("myname")

    :param name: The name to be uploaded.
    :param timeout: The timeout in seconds before the client reports an error.

    :raises NameException if there are any server or transport problems.
    :raises TimeoutError if the request times out.
    :raises TypeError if the type of the name parameter is not string.
    :raises ValueError if the value of the name parameter is ``None``.
    """
    ...