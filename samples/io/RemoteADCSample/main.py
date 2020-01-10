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

IOLINE_IN = IOLine.DIO1_AD1


def main():
    print(" +-------------------------------------+")
    print(" | XBee Gateway Read Remote ADC Sample |")
    print(" +-------------------------------------+\n")

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

        remote_device.set_io_configuration(IOLINE_IN, IOMode.ADC)

        def read_adc_task():
            while not stop:
                # Read the analog value from the remote input line.
                value = remote_device.get_adc_value(IOLINE_IN)
                print("%s: %d" % (IOLINE_IN, value))

                time.sleep(0.2)

        th = threading.Thread(target=read_adc_task)

        time.sleep(0.5)
        th.start()

        input()

    finally:
        stop = True
        if th:
            th.join()
        if local_device is not None and local_device.is_open():
            local_device.close()


if __name__ == '__main__':
    main()
