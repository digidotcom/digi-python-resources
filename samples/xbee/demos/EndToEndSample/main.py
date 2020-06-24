# Copyright (c) 2020, Digi International, Inc.
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

from collections import defaultdict
from digidevice import datapoint, device_request, xbee

MSG_SEPARATOR = "@@@"
MSG_AWAKE = "AWAKE"

DEVICE_REQUEST_TARGET = "tempHum"
DATA_STREAM_TEMP = "%s/temperature"
DATA_STREAM_HUM = "%s/humidity"


def main():
    print(" +--------------------------------+")
    print(" | XBee Gateway End to End Sample |")
    print(" +--------------------------------+\n")

    requests_per_device = defaultdict(list)
    device = xbee.get_device()

    # Callback to handle the data received from other XBee devices.
    def xbee_data_received_callback(msg):
        src_addr = str(msg.remote_device.get_64bit_addr())
        data = msg.data.decode()
        # If the message is an awaken notification, send the pending device requests to that device.
        if data == MSG_AWAKE and src_addr in requests_per_device:
            for request in requests_per_device[src_addr]:
                # Send the request to the remote device.
                device.send_data_async(msg.remote_device, request)
            del requests_per_device[src_addr]
            return

        # If the message is not an awaken notification, ensure it is a temperature/humidity notification.
        data_split = data.split(MSG_SEPARATOR)
        if len(data_split) != 2:
            return

        print("RF data received from %s >> %s" % (src_addr, data))

        # Upload the temperature and humidity values to Digi Remote Manager.
        try:
            datapoint.upload(DATA_STREAM_TEMP % src_addr, data_split[0], units="C",
                             data_type=datapoint.DataType.DOUBLE)
            datapoint.upload(DATA_STREAM_HUM % src_addr, data_split[1], units="%",
                             data_type=datapoint.DataType.DOUBLE)
        except Exception as e:
            print(e)

    # Callback to handle device requests from Digi Remote Manager.
    def drm_request_callback(target, request):
        data = request.strip()
        data_split = data.split(MSG_SEPARATOR)
        if len(data_split) != 2:
            return

        print("Device request received with target %s >> %s" % (target, data))

        dest_addr = data_split[0]
        request = data_split[1]
        requests_per_device[dest_addr].append(request)

    try:
        device.open()

        # Register the callbacks.
        device.add_data_received_callback(xbee_data_received_callback)
        device_request.register(DEVICE_REQUEST_TARGET, drm_request_callback)

        print("Waiting for data...\n")
        input()

    finally:
        # Un-register the callbacks.
        device.del_data_received_callback(xbee_data_received_callback)
        device_request.unregister(DEVICE_REQUEST_TARGET)

        # Close the connection with the device.
        if device.is_open():
            device.close()


if __name__ == '__main__':
    main()
