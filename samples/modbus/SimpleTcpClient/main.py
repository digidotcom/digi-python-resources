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

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ConnectionException

# TODO: Replace with the server IP to connect with.
HOST = "127.0.0.1"
PORT = 5020

# MODBUS UNIT TO ACCESS
UNIT = 0x0


def basic_client():
    client = ModbusTcpClient(HOST, port=PORT)
    try:
        client.write_coil(1, True)
    except ConnectionException as err:
        print("Ensure you have a server running, error: %s" % err)
        return
    result = client.read_coils(1, 1, unit=UNIT)
    print("Result of read_coils is %s" % result.bits[0])
    client.close()


if __name__ == "__main__":
    basic_client()
