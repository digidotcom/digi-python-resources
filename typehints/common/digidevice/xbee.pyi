"""
APIs for accessing the internal XBee module.

This module allows to access the internal XBee module:

    from digidevice import xbee

    XBeeDevice dev = xbee.get_device()

Check the Digi XBee Python library project online for additional information.
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

from digi.xbee.devices import XBeeDevice


def get_device(timeout: int = -1) -> XBeeDevice:
    """
    Gets a representation of the internal XBee device.

    The communication with the internal XBee is not done via serial directly.
    Instead, the XBee Network Manager service is used.
    This service is in charge of synchronizing all access to the internal
    XBee (Web UI, CLI, Python code...).

    Usage::

        xbee.get_device()
        xbee.get_device(timeout=30)

    :param timeout: Maximum amount of time -in seconds- to wait for the internal
        XBee to be ready.

    :return: XBeeDevice handler to the internal XBee device.

    :raises ValueError if the timeout value is too small.
    :raises XBeeException if the internal XBee is not ready.
    """
    ...