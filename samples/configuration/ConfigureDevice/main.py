# Copyright 2023, Digi International Inc.
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

from digidevice import config

CFG_NET_IFACES = "network.interface"
CFG_SYSTEM_DESC = "system.description"

NEW_DEVICE_DESC = "This is the new description of my device"


def main():
    print(" +-------------------------+")
    print(" | Configure Device Sample |")
    print(" +-------------------------+\n")

    # Get the root configuration node just with read permission.
    cfg = config.load()

    # Print all the configuration categories.
    print("All available categories:")
    for category in cfg.keys():
        print(" - %s" % category)
    print("\n")

    # Print the available network interfaces.
    print("Network interfaces category (%s):" % CFG_NET_IFACES)
    for interface in cfg.get(CFG_NET_IFACES).keys():
        print(" - %s" % interface)
    print("\n")

    # Update the device description configuration parameter.
    print("Updating device description...")
    # Get the old device description.
    old_desc = cfg.get(CFG_SYSTEM_DESC)
    # Get the root configuration node with write permission.
    cfg = config.load(writable=True)
    # Set the new system description.
    cfg.set(CFG_SYSTEM_DESC, NEW_DEVICE_DESC)
    cfg.commit()
    # Get the root configuration node just with read permission.
    cfg = config.load()
    # Get the new device description.
    new_desc = cfg.get(CFG_SYSTEM_DESC)
    # Compare descriptions.
    print(" - Old description: %s" % old_desc)
    print(" - New description: %s" % new_desc)


if __name__ == "__main__":
    main()
