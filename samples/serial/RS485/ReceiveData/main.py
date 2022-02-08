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

import time
import serial
import serial.rs485

# TODO: Replace with the serial port used to receive data.
PORT = "/dev/serial/port1"
# TODO: Replace with the preferred baud rate.
BAUD_RATE = 9600

# Optional serial settings
STOP_BITS = serial.STOPBITS_ONE
N_DATA_BITS = 8
PARITY = serial.PARITY_NONE
RTS_CTS = 0

# RS485 specific settings
RS485_RTS_ON_SEND = False
RS485_RTS_AFTER_SEND = True
RS485_RX_DURING_TX = False
RS485_DELAY_BEFORE_TX = 0.01
RS485_DELAY_BEFORE_RX = 0.01


def main():
    # Create and configure the serial port settings
    ser = serial.Serial()
    ser.baudrate = BAUD_RATE
    ser.port = PORT
    ser.stopbits = STOP_BITS
    ser.bytesize = N_DATA_BITS
    ser.parity = PARITY
    ser.rtscts = RTS_CTS

    # Configure specific RS485 settings
    ser.rs485_mode = serial.rs485.RS485Settings()
    ser.rs485_mode.rts_level_for_tx = RS485_RTS_ON_SEND
    ser.rs485_mode.rts_level_for_rx = RS485_RTS_AFTER_SEND
    ser.rs485_mode.loopback = RS485_RX_DURING_TX
    ser.rs485_mode.delay_before_tx = RS485_DELAY_BEFORE_TX
    ser.rs485_mode.delay_before_rx = RS485_DELAY_BEFORE_RX

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
