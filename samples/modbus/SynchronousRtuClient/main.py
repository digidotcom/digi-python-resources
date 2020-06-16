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

import logging
import serial
import serial.rs485

from pymodbus.client.sync import ModbusSerialClient as ModbusClient

# Modbus RTU settings
# TODO: Replace with the serial port to use.
PORT = "/dev/ttymxc2"
# TODO: Replace with the preferred baud rate.
BAUD_RATE = 9600

# Optional RTU serial settings
STOP_BITS = serial.STOPBITS_ONE
N_DATA_BITS = 8
PARITY = serial.PARITY_NONE

# Modbus unit to access
UNIT = 0x1

FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')

# Configure the client logging
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def configure_port_in_rs485_mode():
    # Create and configure the serial port settings
    ser = serial.Serial()
    ser.baudrate = BAUD_RATE
    ser.port = PORT

    # Configure specific RS485 settings
    ser.rs485_mode = serial.rs485.RS485Settings()
    ser.rs485_mode.rts_level_for_tx = False
    ser.rs485_mode.rts_level_for_rx = True
    ser.rs485_mode.loopback = False

    # Open and close the serial port to apply the settings
    ser.open()
    ser.close()


def run_sync_client():
    client = ModbusClient(method='rtu', port=PORT, timeout=1, baudrate=BAUD_RATE,
                          parity=PARITY, stopbits = STOP_BITS, bytesize = N_DATA_BITS)
    client.connect()

    # ------------------------------------------------------------------------#
    # Specify slave to query
    # ------------------------------------------------------------------------#
    # The slave to query is specified in an optional parameter for each
    # individual request. This can be done by specifying the `unit` parameter
    # which defaults to `0x00`
    # ----------------------------------------------------------------------- #
    log.debug("Read coils")
    read_resp = client.read_coils(1, 1, unit=UNIT)
    log.debug(read_resp)

    # ----------------------------------------------------------------------- #
    # Example requests
    # ----------------------------------------------------------------------- #
    # simply call the methods that you would like to use. An example session
    # is displayed below along with some assert checks. Note that some Modbus
    # implementations differentiate holding/input discrete/coils and as such
    # you will not be able to write to these, therefore the starting values
    # are not known to these tests. Furthermore, some use the same memory
    # blocks for the two sets, so a change to one is a change to the other.
    # Keep both of these cases in mind when testing as the following will
    # _only_ pass with the supplied asynchronous Modbus server (script supplied).
    # ----------------------------------------------------------------------- #
    log.debug("Write to a coil and read back")
    write_resp = client.write_coil(0, True, unit=UNIT)
    read_resp = client.read_coils(0, 1, unit=UNIT)
    assert not write_resp.isError()        # test that we are not an error
    assert read_resp.bits[0]               # test the expected value

    log.debug("Write to multiple coils and read back- test 1")
    write_resp = client.write_coils(1, [True]*8, unit=UNIT)
    assert not write_resp.isError()        # test that we are not an error
    read_resp = client.read_coils(1, 21, unit=UNIT)
    assert not read_resp.isError()         # test that we are not an error
    resp = [True]*21

    # If the returned output quantity is not a multiple of eight,
    # the remaining bits in the final data byte will be padded with zeros
    # (toward the high order end of the byte)

    resp.extend([False]*3)
    assert read_resp.bits == resp          # test the expected value

    log.debug("Write to multiple coils and read back - test 2")
    write_resp = client.write_coils(1, [False]*8, unit=UNIT)
    read_resp = client.read_coils(1, 8, unit=UNIT)
    assert not write_resp.isError()        # test that we are not an error
    assert read_resp.bits == [False]*8     # test the expected value

    log.debug("Read discrete inputs")
    read_resp = client.read_discrete_inputs(0, 8, unit=UNIT)
    assert not write_resp.isError()        # test that we are not an error

    log.debug("Write to a holding register and read back")
    write_resp = client.write_register(1, 10, unit=UNIT)
    read_resp = client.read_holding_registers(1, 1, unit=UNIT)
    assert not write_resp.isError()        # test that we are not an error
    assert read_resp.registers[0] == 10    # test the expected value

    log.debug("Write to multiple holding registers and read back")
    write_resp = client.write_registers(1, [10]*8, unit=UNIT)
    read_resp = client.read_holding_registers(1, 8, unit=UNIT)
    assert not write_resp.isError()        # test that we are not an error
    assert read_resp.registers == [10]*8   # test the expected value

    log.debug("Read input registers")
    read_resp = client.read_input_registers(1, 8, unit=UNIT)
    assert not write_resp.isError()        # test that we are not an error

    arguments = {
        'read_address':    1,
        'read_count':      8,
        'write_address':   1,
        'write_registers': [20]*8,
    }
    log.debug("Read write registers simultaneously")
    write_resp = client.readwrite_registers(unit=UNIT, **arguments)
    read_resp = client.read_holding_registers(1, 8, unit=UNIT)
    assert not write_resp.isError()        # test that we are not an error
    assert write_resp.registers == [20]*8  # test the expected value
    assert read_resp.registers == [20]*8   # test the expected value

    # ----------------------------------------------------------------------- #
    # Close the client
    # ----------------------------------------------------------------------- #
    client.close()


if __name__ == "__main__":
    configure_port_in_rs485_mode()
    run_sync_client()
