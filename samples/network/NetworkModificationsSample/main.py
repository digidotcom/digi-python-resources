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

import time

from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import RemoteXBeeDevice
from digidevice import xbee


def callback_discovery_finished(status):
    if status == NetworkDiscoveryStatus.SUCCESS:
        print("  Discovery process finished successfully.")
    else:
        print("  There was an error discovering devices: %s" % status.description)


def cb_network_modified(event_type, reason, node):
    print("  >>>> Network event:")
    print("         Type: %s (%d)" % (event_type.description, event_type.code))
    print("         Reason: %s (%d)" % (reason.description, reason.code))

    if not node:
        return

    print("         Node:")
    print("            %s" % node)


def print_nodes(xb_net):
    print("\n  Current network nodes:\n    ", end='')
    if xb_net.has_devices():
        print("%s" % '\n    '.join(map(str, xb_net.get_devices())))
    else:
        print("None")


def main():
    print(" +---------------------------------------------------+")
    print(" | XBee Gateway Network modifications Devices Sample |")
    print(" +---------------------------------------------------+\n")

    device_network = None

    device = xbee.get_device()

    try:
        device.open()

        device_network = device.get_network()

        device_network.set_discovery_timeout(15)  # 15 seconds.

        device_network.add_discovery_process_finished_callback(callback_discovery_finished)

        device_network.add_network_modified_callback(cb_network_modified)

        print("* Discover remote XBee devices...")

        device_network.start_discovery_process()

        while device_network.is_discovery_running():
            time.sleep(1)

        print_nodes(device_network)

        print("\n* Manually add a new remote XBee device...")
        remote = RemoteXBeeDevice(
            device,
            x64bit_addr=XBee64BitAddress.from_hex_string("1234567890ABCDEF"),
            node_id="manually_added")
        device_network.add_remote(remote)

        print_nodes(device_network)

        time.sleep(1)

        print("\n* Update the last added remote XBee device...")
        remote = RemoteXBeeDevice(device, x64bit_addr=remote.get_64bit_addr(), node_id="updated_node")
        device_network.add_remote(remote)

        print_nodes(device_network)

        time.sleep(1)

        print("\n* Manually remove a remote XBee device...")
        device_network.remove_device(remote)

        print_nodes(device_network)

        time.sleep(1)

        print("\n* Clear network...")
        device_network.clear()

        print_nodes(device_network)

    finally:
        if device_network is not None:
            device_network.del_discovery_process_finished_callback(callback_discovery_finished)
            device_network.del_network_modified_callback(cb_network_modified)

        if device.is_open():
            device.close()


if __name__ == '__main__':
    main()
