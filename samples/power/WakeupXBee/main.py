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

from digidevice import cli, config, xbee

CFG_WAKEUP_XBEE = "system.power.wakeup_sources.xbee"
CLI_SUSPEND = "powerctrl state suspend"


def main():
    # Configure the XBee interface as a wake up source
    cfg = config.load(writable=True)
    old_wake_xbee = cfg.get(CFG_WAKEUP_XBEE)
    cfg.set(CFG_WAKEUP_XBEE, True)
    cfg.commit()

    # Give time to the configuration scripts to execute
    time.sleep(2)

    # Open the XBee interface and register a receive data callback
    device = xbee.get_device()
    try:
        device.open()

        def data_receive_callback(xbee_message):
            print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
                                     xbee_message.data.decode()))

        device.add_data_received_callback(data_receive_callback)

        # Suspend the device
        print("Going to suspend...")
        print(cli.execute(CLI_SUSPEND))

        # At this point device is awake, print a message
        print("Device is awake!")

        # Remove the XBee data listener
        device.del_data_received_callback(data_receive_callback)
    finally:
        # Close the XBee interface
        if device.is_open():
            device.close()

        # Restore the old wake up XBee value
        cfg = config.load(writable=True)
        cfg.set(CFG_WAKEUP_XBEE, old_wake_xbee)
        cfg.commit()


if __name__ == '__main__':
    main()
