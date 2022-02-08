# Copyright 2020-2022, Digi International Inc.
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

# TODO: Replace with the serial port used to send data.
PORT = "/dev/serial/port1"
# TODO: Replace with the preferred baud rate.
BAUD_RATE = 9600

# Optional serial settings
STOP_BITS = serial.STOPBITS_ONE
N_DATA_BITS = 8
PARITY = serial.PARITY_NONE
RTS_CTS = 0

DATA_TO_SEND = "Hello from RS232 TX side"


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

    # Send data thought the serial port
    ser.write(DATA_TO_SEND.encode())

    # Flush any pending data and close the serial port
    ser.flush()
    ser.close()


if __name__ == '__main__':
    main()
