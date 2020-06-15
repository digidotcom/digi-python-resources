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
import serial

# TODO: Replace with the serial port used to receive data.
PORT = "/dev/ttymxc2"
# TODO: Replace with the preferred baud rate.
BAUD_RATE = 9600

# Optional serial settings
STOP_BITS = serial.STOPBITS_ONE
N_DATA_BITS = 8
PARITY = serial.PARITY_NONE
RTS_CTS = 0


def main():
    # Create and configure the serial port settings
    ser = serial.Serial()
    ser.baudrate = BAUD_RATE
    ser.port = PORT
    ser.stopbits = STOP_BITS
    ser.bytesize = N_DATA_BITS
    ser.parity = PARITY
    ser.rtscts = RTS_CTS

    # Open the serial port
    ser.open()

    # Receive data from the serial port until ctrl-c is pressed
    try:
        while True:
            if ser.in_waiting:
                print(ser.read(ser.in_waiting).decode(), end="", flush=True)
            time.sleep(0.01)
    except KeyboardInterrupt:
        # Close the serial port
        ser.close()


if __name__ == '__main__':
    main()
