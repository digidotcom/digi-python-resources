# Copyright 2020, Digi International Inc.
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

from digi.xbee.io import IOLine, IOMode
from digidevice import xbee
import time
import threading

REMOTE_NODE_ID = "REMOTE"

IOLINE_IN = IOLine.DIO3_AD3
IOLINE_OUT = IOLine.DIO4_AD4


def main():
    print(" +----------------------------------------+")
    print(" | XBee Gateway Get/Set Remote DIO Sample |")
    print(" +----------------------------------------+\n")

    stop = False
    th = None

    local_device = xbee.get_device()

    try:
        local_device.open()

        # Obtain the remote XBee device from the XBee network.
        xbee_network = local_device.get_network()
        remote_device = xbee_network.get_device_by_node_id(REMOTE_NODE_ID)
        if not remote_device:
            print("Device not found in the network, trying to discover it...")
            remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
        if remote_device is None:
            print("Could not discover the remote device")
            exit(1)

        def io_detection_callback():
            while not stop:
                # Read the digital value from the input line.
                io_value = remote_device.get_dio_value(IOLINE_IN)
                print("%s: %s" % (IOLINE_IN, io_value))

                # Set the previous value to the local output line.
                local_device.set_dio_value(IOLINE_OUT, io_value)

                time.sleep(0.2)

        th = threading.Thread(target=io_detection_callback)

        remote_device.set_io_configuration(IOLINE_IN, IOMode.DIGITAL_IN)

        local_device.set_io_configuration(IOLINE_OUT, IOMode.DIGITAL_OUT_LOW)

        time.sleep(0.5)
        th.start()

        input()

    finally:
        stop = True
        if th is not None and th.is_alive():
            th.join()
        if local_device is not None and local_device.is_open():
            local_device.close()


if __name__ == '__main__':
    main()
