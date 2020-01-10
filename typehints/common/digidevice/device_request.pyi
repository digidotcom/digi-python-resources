"""
APIs for registering device request handlers.

This module allows to register callbacks for SCI device requests
from DRM:

    from digidevice import device_request
    
    def handler(target, request):
        print("I received request %s for target %s", request, target)
        print("Sending OK response")
        return "OK"

    device_request.register("my_target", handler)

Check help(device_request.register) and help(device_request.unregister)
for more details and parameters.
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

from typing import Callable, Optional


class DeviceRequestException(RuntimeError):
    """
    Exception generated when a callback fails to be registered. Its message
    contains the description of the problem.
    """

    def __init__(self, msg: str) -> None:
        """
        Class constructor. Instantiates a new ``DeviceRequestException`` object
        with the provided parameters.

        :param msg: The message containing the description of the problem.
        """
        ...


def register(target: str, response_callback: Callable[[str, str],
                                                      Optional[str]],
             status_callback: Optional[Callable[[int, str], None]] = None,
             xml_encoding: str = "UTF-8") -> None:
    """
    Registers a callback function for a Digi Remote Manager SCI device request
    for a given target.
    The registered callback will be called when the device receives a SCI device
    request for the given target. This callback may return a str (or
    str-convertible object) that will be sent back to Digi Remote Manager as
    response to the SCI device request.
    Optionally, a second callback to receive information about the SCI response
    sent may be passed.
    The default encoding for SCI device request is UTF-8, but a different
    encoding may be specified. If the encoding is set to None or the decoding
    of a request from DRM fails, the response_callback function will be called
    with the raw byte array as a parameter, instead of a str.
    For the response_callback return value, characters that cannot be encoded
    in the given encoding will be replaced.
    Note that only one callback can be associated to any given target: when this
    method is called with a target that is already registered, the old callback
    will be overridden and no longer called. This applies even if the previous
    call to .register was done from a different process.

    Example of RCI request for target "myTarget":
    <sci_request version="1.0">
       <data_service>
         <targets>
           <device id="00000000-00000000-00000000-00000000"/>
         </targets>
         <requests>
              <device_request target_name="myTarget">my payload string</device_request>
         </requests>
       </data_service>
    </sci_request>

    Usage::

        device_request.register("my_target", my_handler)
        device_request.register("my_target", my_handler, status_callback = my_status_cb)
        device_request.register("my_bin_target", my_bin_handler, xml_encoding = None)

    :param target: Value of the "target_name" attribute on the SCI
        device_request.
    :param response_callback: callback function that takes two arguments: the
        target (str) and the request (str). The function may return a string to
        be sent back to Digi Remote Manager as a reply to the SCI request.
    :param status_callback: Optional: callback function that provides status
        about the SCI reply. It takes two arguments: an error code (int) that
        is either 0 for success, or other positive values for different errors
        and an error hint (str) that contains an indication of the problem or
        "Success" for error code 0.
    :param xml_encoding: Optional: Encoding for the SCI request. In case the
        raw bytes cannot be interpreted using the specified encoding, or if the
        specified encoding is ``None``, the response_callback will be invoked
        with the raw byte array instead of the str for the request argument.
        For the response_callback return value, characters that cannot be
        encoded in the given encoding will be replaced. Defaults to UTF-8.

    :raises DeviceRequestException if there are any server or transport
        problems.
    :raises TimeoutError if the request times out.
    :raises TypeError if the type of any parameter does not match the expected
        one.
    """
    ...


def unregister(target: str) -> bool:
    """
    Unregisters a previously registered callback for a given SCI target.

    Note that you cannot unregister callbacks which were registered by another
    process.

    Usage::
        device_request.unregister("my_target")

    :param target: Value of the "target_name" attribute on the SCI
        device_request to it by the server.

    :return: ``True`` if the target was unregistered, ``False`` otherwise or if
        the target was not registered by this process.

    :raises DeviceRequestException if there are any server or transport
        problems.
    :raises TimeoutError if the request times out.
    :raises TypeError if the type of any parameter doesn't match the expected
        one.
    """
    ...