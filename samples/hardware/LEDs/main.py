# Copyright 2021, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from digidevice import led
from digidevice.led import Led, State
import time

# Create XBee RGB LEDs vars
XBEE_RED = Led.XBEE1
XBEE_GREEN = Led.XBEE2
XBEE_BLUE = Led.XBEE3


def main():
    # Acquire exclusive Python access to XBee LEDs
    led.acquire(XBEE_RED)
    led.acquire(XBEE_GREEN)
    led.acquire(XBEE_BLUE)

    # Switch XBee LED off for 5 seconds
    print("Setting XBee LED OFF for 5 seconds...")
    led.set(XBEE_RED, State.OFF)
    led.set(XBEE_GREEN, State.OFF)
    led.set(XBEE_BLUE, State.OFF)
    time.sleep(5)

    # Set XBee LED to RED for 5 seconds
    print("Setting XBee LED RED for 5 seconds...")
    led.set(XBEE_RED, State.ON)
    time.sleep(5)

    # Set XBee LED to GREEN for 5 seconds
    print("Setting XBee LED GREEN for 5 seconds...")
    led.set(XBEE_RED, State.OFF)
    led.set(XBEE_GREEN, State.ON)
    time.sleep(5)

    # Set XBee LED to BLUE for 5 seconds
    print("Setting XBee LED BLUE for 5 seconds...")
    led.set(XBEE_GREEN, State.OFF)
    led.set(XBEE_BLUE, State.ON)
    time.sleep(5)

    # Blink XBee LED in WHITE for 10 seconds
    print("Blinking XBee LED WHITE for 10 seconds...")
    led.set(XBEE_RED, State.FLASH)
    led.set(XBEE_GREEN, State.FLASH)
    led.set(XBEE_BLUE, State.FLASH)
    time.sleep(10)

    # Return XBee LEDs control to the system
    led.release(XBEE_RED)
    led.release(XBEE_GREEN)
    led.release(XBEE_BLUE)


if __name__ == '__main__':
    main()
