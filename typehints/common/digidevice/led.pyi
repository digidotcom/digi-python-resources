"""
APIs for controlling the device's LEDs.

This module allows control of the device's LEDs:

    from digidevice import led
    from digidevice.led import Led, State

    # Method 1:
    with led.use(Led.POWER) as pwr:
        pwr(State.ON)

    # Method 2:
    led.acquire(Led.POWER)
    led.set(Led.POWER, State.ON)
    led.release(Led.POWER)

Check help(led.acquire), help(led.set), help(led.release), or help(led.use)
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
import enum
from contextlib import contextmanager
from enum import Enum
from typing import Generator


class LedException(Exception):
    """
    Exception generated if a problem occurs when managing an LED.
    """
    ...


def acquire(led: Enum) -> None:
    """
    Acquires an LED for exclusive control by Python.

    Usage::

        led.acquire(Led.POWER)

    :param led: The LED to be acquired.

    :raises LedException if the LED is already being used by another process or
        if there is any other problem acquiring it.
    """
    ...


def release(led: Enum) -> None:
    """
    Releases an LED back for control by the system.

    Usage::

        led.release(Led.POWER)

    :param led: The LED to be released.

    :raises LedException if the LED was never acquired for use or if there is any
        other problem releasing it.
    """
    ...


def set(led: Enum, state: Enum) -> None:
    """
    Sets an LED to the given state.

    Usage::

        led.set(Led.POWER, State.ON)

    :param led: The LED to be set.
    :param state: The required LED state.

    :raises LedException if there was any problem setting the state of the LED.
    """
    ...

@contextmanager
def use(led: Enum) -> Generator[None, None, None]:
    """
    Acquires an LED for exclusive use by Python, and release back to the system
    for control during cleanup. Yields a set function for that LED, which
    accepts a State 

    Usage::

        with use(Led.POWER) as pwr:
            pwr(State.ON)

    :param led: The LED to use.

    :return: A bound function representing the LED that accepts a single State 
        parameter to set the LED to.

    :raises LedException if there was any problem either acquiring, releasing or
        setting the state of the LED.
    """
    ...

class Led(Enum):
    """
    Lists all the available LED types.
    """
    POWER = ...
    GNSS = ...
    WIFI1 = ...
    WIFI2 = ...
    WWAN1_SIGNAL_GREEN = ...
    WWAN1_SIGNAL_YELLOW = ...
    WWAN1_SERVICE_GREEN = ...
    WWAN1_SERVICE_YELLOW = ...
    WWAN2_SIGNAL_GREEN = ...
    WWAN2_SIGNAL_YELLOW = ...
    WWAN2_SERVICE_GREEN = ...
    WWAN2_SERVICE_YELLOW = ...
    ALL = ...

class State(Enum):
    """
    Lists all the available LED states.
    """
    ON = ...
    OFF = ...
    FLASH_SLOW = ...
    FLASH_FAST = ...
