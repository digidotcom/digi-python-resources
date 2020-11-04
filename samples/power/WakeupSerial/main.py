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

import serial
import time

from digidevice import cli, config

# TODO: Replace with the desired serial port parameters.
PORT = "/dev/serial/port1"
BAUD_RATE = 9600
STOP_BITS = serial.STOPBITS_ONE
N_DATA_BITS = serial.EIGHTBITS
PARITY = serial.PARITY_NONE
RTS_CTS = False

CFG_WAKEUP_SERIAL = "system.power.wakeup_sources.serial"
CLI_SUSPEND = "powerctrl state suspend"


def main():
    # Configure the Serial port as a wake up source
    cfg = config.load(writable=True)
    old_wake_serial = cfg.get(CFG_WAKEUP_SERIAL)
    cfg.set(CFG_WAKEUP_SERIAL, True)
    cfg.commit()

    # Give time to the configuration scripts to execute
    time.sleep(2)

    # Create and configure the serial port settings
    ser = serial.Serial()
    ser.baudrate = BAUD_RATE
    ser.bytesize = N_DATA_BITS
    ser.stopbits = STOP_BITS
    ser.parity = PARITY
    ser.rtscts = RTS_CTS
    ser.timeout = 0.1
    ser.setPort(PORT)

    # Open the serial port
    ser.open()

    # Suspend the device
    print("Going to suspend...", flush=True)
    print(cli.execute(CLI_SUSPEND))

    # At this point device is awake, print a message
    print("Device is awake!")

    # Close the serial port
    ser.close()

    # Restore the old wake up serial value
    cfg = config.load(writable=True)
    cfg.set(CFG_WAKEUP_SERIAL, old_wake_serial)
    cfg.commit()


if __name__ == '__main__':
    main()
