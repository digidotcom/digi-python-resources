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

from digidevice import xbee

DATA_TO_SEND = "Hello XBee!"
REMOTE_NODE_ID = "REMOTE"


def main():
    print(" +----------------------------------------------+")
    print(" | XBee Gateway Send Data Asynchronously Sample |")
    print(" +----------------------------------------------+\n")

    device = xbee.get_device()

    try:
        device.open()

        # Obtain the remote XBee device from the XBee network.
        xbee_network = device.get_network()
        remote_device = xbee_network.get_device_by_node_id(REMOTE_NODE_ID)
        if not remote_device:
            print("Device not found in the network, trying to discover it...")
            remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
        if remote_device is None:
            print("Could not discover the remote device")
            exit(1)

        print("Sending data asynchronously to %s >> %s..." % (remote_device.get_64bit_addr(), DATA_TO_SEND))

        device.send_data_async(remote_device, DATA_TO_SEND)

        print("Success")

    finally:
        if device.is_open():
            device.close()


if __name__ == '__main__':
    main()
