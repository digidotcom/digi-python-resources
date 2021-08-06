# Copyright (c) 2021, Digi International, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time

from digidevice import datapoint, runt
from digidevice.datapoint import DataType

DATA_STREAM_TEMP = "single_temperature"

PROP_TEMPERATURE = "system.cpu_temp"


def main():
    print(" +---------------------------------------------------+")
    print(" | Digi Remote Manager Send Single Data Point Sample |")
    print(" +---------------------------------------------------+\n")

    runt.start()

    # Read the temperature and upload it to Digi Remote Manager every 10 seconds
    # during a minute.
    for i in range(6):
        # Read the temperature from runt.
        temp_data = round(float(runt.get(PROP_TEMPERATURE).split(" ")[0]), 2)
        # Upload the temperature to Digi Remote Manager.
        print("Uploading temperature %s..." % temp_data)
        try:
            datapoint.upload(DATA_STREAM_TEMP, temp_data, units="C", data_type=DataType.FLOAT)
        except Exception as e:
            print(e)
        time.sleep(10)

    runt.stop()


if __name__ == '__main__':
    main()
