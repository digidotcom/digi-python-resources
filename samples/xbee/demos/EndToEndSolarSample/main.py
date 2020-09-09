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

import json
import os
import random
import time
import traceback
from datetime import datetime
from json import JSONDecodeError
from threading import Timer

from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.exception import XBeeException
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.models.mode import APIOutputMode
from digi.xbee.packets.aft import ApiFrameType
from digi.xbee.util import utils
from digidevice import datapoint, device_request, runt, xbee

# Constants.
DRM_TARGET_AUTO_FOLLOW = "auto_follow"
DRM_TARGET_RESET_POSITION = "reset_position"
DRM_TARGET_SAMPLING_RATE = "sampling_rate"

ITEM_OP = "operation"
ITEM_STATUS = "status"
ITEM_MSG = "error_message"
ITEM_VALUE = "value"
ITEM_MAC = "mac"
ITEM_PROP = "properties"

PROP_LATITUDE = "latitude"
PROP_LONGITUDE = "longitude"
PROP_ALTITUDE = "altitude"
PROP_ROW = "row"
PROP_COLUMN = "column"
PROP_NAME = "name"
PROP_PAN_ID = "pan_id"
PROP_PASS = "password"
PROP_MAIN_CONTROLLER = "main_controller"

OP_ID = "id"
OP_READ = "read"
OP_WRITE = "write"
OP_FINISH = "finish"

STATUS_SUCCESS = "success"
STATUS_ERROR = "error"

VALUE_ID = "gateway"

FILE_MAIN_CONTROLLER = "./is_main_controller"

CMD_ID_RECV = 0
CMD_ID_SET = 1

ID_REPORT_INTERVAL = 0
SENS_ID_PANEL_TEMP = 1
SENS_ID_PANEL_POSITION = 2
SENS_ID_PANEL_RADIATION = 3
SENS_ID_CONT_WIND = 4
SENS_ID_CONT_LIGHT = 5
SENS_ID_CONT_RADIATION = 6

POSITION_MAX = 270000  # 270.0º
POSITION_MIN = 90000   # 90.0º

WIND_MAX = 120000       # 120.0 km/h
WIND_MIN = 0            # 0.0 km/h
WIND_DELTA = 2000       # 2.0 km/h
WIND_THRESHOLD = 80000  # 80.0 km/h

LIGHT_MAX = 100000000  # 100000.0 lx
LIGHT_MIN = 30000000   # 30000.0 lx
LIGHT_DELTA = 500000   # 500.0 lx

RADIATION_DELTA = 10000  # 10.0 W/m2

DEFAULT_POS = 180000        # 180º
DEFAULT_WIND = 5000         # 5.0 km/h
DEFAULT_LIGHT = 75000000    # 75000.0 lx
DEFAULT_RADIATION = 350000  # 350.0 W/m2

WIND_ALARM_POS = 0  # Alarm position (totally horizontal, like 180º)

DEFAULT_REPORT_INTERVAL = 60  # 1 minute
POSITIONS_INTERVAL = 30  # 30 seconds

MIN_PAYLOAD_SIZE = 7  # cmd + sum samples + sensor id + sensor data (4) = 7
MIN_DRM_REQUEST_ADDR_SIZE = 16

DATA_STREAM_FORMAT = "{}/{}"

AT_CMD_BT = "BT"  # Bluetooth Enable
AT_CMD_CE = "CE"  # Device Role
AT_CMD_EE = "EE"  # Encryption Enable
AT_CMD_ID = "ID"  # Extended PAN ID
AT_CMD_KY = "KY"  # Link Key
AT_CMD_LX = "LX"  # Location X - Latitude
AT_CMD_LY = "LY"  # Location Y - Longitude
AT_CMD_LZ = "LZ"  # Location Z - Elevation
AT_CMD_NI = "NI"  # Node Identifier

AT_VALUE_DISABLED = "0"
AT_VALUE_ENABLED = "1"

XBEE_PROPERTIES = {
    PROP_LATITUDE:  AT_CMD_LX,
    PROP_LONGITUDE: AT_CMD_LY,
    PROP_ALTITUDE:  AT_CMD_LZ,
    PROP_NAME:      AT_CMD_NI,
    PROP_PAN_ID:    AT_CMD_ID,
    PROP_PASS:      AT_CMD_KY,
}

XBEE_TEXT_PROPERTIES = [
    PROP_NAME,
    PROP_LATITUDE,
    PROP_LONGITUDE,
    PROP_ALTITUDE
]

# Variables.
device = None

wind = DEFAULT_WIND
light = DEFAULT_LIGHT
radiation = DEFAULT_RADIATION

auto_follow = True
auto_follow_dict = dict()

report_interval = DEFAULT_REPORT_INTERVAL


def bluetooth_data_callback(data):
    """
    Callback executed every time the XBee module receives data from the
    Bluetooth interface.
    Processes the incoming data in JSON format, executes the appropriate action
    and responds to the Bluetooth device if required.

    Args
        data (Bytearray): the received data.
    """
    response = {}

    # Parse the JSON items
    try:
        json_items = json.loads(data.decode())
    except JSONDecodeError:
        return

    # Get the operation to perform.
    operation = json_items[ITEM_OP]
    if operation == OP_ID:
        # Set the response command ID.
        response[ITEM_OP] = OP_ID
        response[ITEM_STATUS] = STATUS_SUCCESS
        response[ITEM_VALUE] = VALUE_ID
        response[ITEM_MAC] = get_runt("system.mac")
    elif operation == OP_WRITE:
        # Set the response command ID.
        response[ITEM_OP] = OP_WRITE
        # Write the given properties.
        success = save_properties(json_items[ITEM_PROP])
        if success:
            response[ITEM_STATUS] = STATUS_SUCCESS
        else:
            response[ITEM_STATUS] = STATUS_ERROR
            response[ITEM_MSG] = "Error writing settings to the XBee module."
    elif operation == OP_FINISH:
        finish_provisioning()
        return
    else:
        return

    # Send back the response.
    device.send_bluetooth_data(json.dumps(response).encode())


def drm_request_callback(target, request):
    """
    Callback executed every time the solar controller receives a device request
    from Digi Remote Manager.
    Processes the incoming request depending on the target and executes the
    corresponding action.

    Args:
        target (String): the device request target.
        request (String): the device request.
    """
    dest_addr = None
    data = request

    # Check if the request is for a specific solar panel or for all.
    if len(request) >= MIN_DRM_REQUEST_ADDR_SIZE:
        dest_addr = request[0:MIN_DRM_REQUEST_ADDR_SIZE]
        data = request[MIN_DRM_REQUEST_ADDR_SIZE:len(request)]

    # Execute the corresponding action based on the target.
    if target == DRM_TARGET_AUTO_FOLLOW:
        set_auto_follow(data, dest_addr)
    elif target == DRM_TARGET_RESET_POSITION:
        reset_position(dest_addr)
    elif target == DRM_TARGET_SAMPLING_RATE:
        set_report_interval(int(data))


def xbee_data_callback(msg):
    """
    Callback executed every time the XBee device receives data from another
    device of the XBee network.
    Processes the incoming message and uploads the sensor readings to Digi
    Remote Manager.

    Args:
        msg (:class:`XBeeMessage`): the XBee message containing the sender and
            the data.
    """
    sender = str(msg.remote_device.get_64bit_addr())
    data_list = list(msg.data)

    # If the sender is not in the auto-follow dictionary, add it with the default value.
    if sender not in auto_follow_dict:
        auto_follow_dict[sender] = auto_follow

    if msg.is_broadcast or len(data_list) < MIN_PAYLOAD_SIZE or data_list[0] != CMD_ID_RECV:
        return

    print_log("Sensor data received from '{}' with payload '{}'".format(sender, data_list))

    # Parse the configurations contained in the message and upload them to DRM.
    configurations = parse_configurations(data_list)
    for configuration in configurations:
        upload_configuration_drm(configuration, sender)


def xbee_packet_callback(packet):
    """
    Callback executed every time the XBee device receives an XBee packet.
    The solar panels send a packet every time they join to the XBee network,
    so this method processes those packets in order to keep the list of remote
    devices up to date.

    Args:
        packet (:class:`XBeeAPIPacket`): the packet received.
    """
    if packet.get_frame_type() == ApiFrameType.EXPLICIT_RX_INDICATOR:
        sender = str(packet.x64bit_source_addr)
        # If the sender is not in the auto-follow dictionary, add it with the default value.
        if sender not in auto_follow_dict:
            auto_follow_dict[sender] = auto_follow


def save_properties(properties):
    """
    Saves the given properties in the XBee firmware of the device.

    Args:
        properties (dict): dictionary containing the properties to save.

    Returns:
        ``True`` if the properties were saved successfully, ``False``
        otherwise.
    """
    global is_main_controller

    # Save XBee properties in the XBee firmware.
    try:
        for prop in XBEE_PROPERTIES:
            # Skip empty settings.
            if prop not in properties or properties[prop] is None:
                continue
            print_log("Saving property '{}' with '{}' in the XBee device".format(prop, properties[prop]))

            at_cmd = XBEE_PROPERTIES[prop]
            value = properties[prop].encode() if prop in XBEE_TEXT_PROPERTIES \
                else utils.hex_string_to_bytes(properties[prop])
            device.set_parameter(at_cmd, value)

        # When configuring the PAN ID, set the XBee role as coordinator.
        if PROP_PAN_ID in properties:
            device.set_parameter(AT_CMD_CE, utils.hex_string_to_bytes(AT_VALUE_ENABLED))
        # When configuring the network password, enable the encryption.
        if PROP_PASS in properties:
            device.set_parameter(AT_CMD_EE, utils.hex_string_to_bytes(AT_VALUE_ENABLED))

        write_xbee_settings()

        # Check if this is the main controller.
        set_main_controller(PROP_MAIN_CONTROLLER in properties)

        return True
    except Exception as e:
        print(e)
        traceback.print_exc()

    return False


def write_xbee_settings():
    """
    Applies and writes the configured XBee settings.
    """
    device.apply_changes()
    device.write_changes()


def set_main_controller(is_main):
    """
    Sets whether this is the main controller or not.

    Args:
        is_main (Boolean): ``True`` to set this the main controller, ``False``
            otherwise.
    """
    if is_main:
        open(FILE_MAIN_CONTROLLER, "w").close()
    elif os.path.exists(FILE_MAIN_CONTROLLER):
        os.remove(FILE_MAIN_CONTROLLER)


def is_main_controller():
    """
    Returns whether this is the main controller or not.

    Returns:
        ``True`` if this is the main controller, ``False`` otherwise.
    """
    return os.path.exists(FILE_MAIN_CONTROLLER)


def finish_provisioning():
    """
    Finishes the provisioning phase by disabling the Bluetooth interface.
    """
    # Disable the Bluetooth interface.
    device.set_parameter(AT_CMD_BT, utils.hex_string_to_bytes("0"))
    write_xbee_settings()


def set_auto_follow(follow, dest_addr=None):
    """
    Sets whether the solar panel with the given address (or all if none is
    specified) should follow the sun position or not.

    Args:
        follow (Boolean): ``True`` to auto-follow the sun position, ``False``
            otherwise.
        dest_addr (String, optional): the 64-bit address of the solar panel the
            auto-follow property will be applied to. If none is specified, it
            will be applied to all panels.
    """
    global auto_follow

    follow_value = follow == "1"

    # Update the value in the dictionary.
    if dest_addr is not None:
        auto_follow_dict[dest_addr] = follow_value
    else:
        auto_follow = follow_value
        for dev in auto_follow_dict:
            auto_follow_dict[dev] = follow_value

    print_log("Auto-follow sun {} ({})".format("enabled" if follow_value else "disabled",
                                               dest_addr if dest_addr is not None else "ALL"))


def reset_position(dest_addr=None):
    """
    Resets the position of the solar panel with the given 64-bit address (or
    all if none is specified).

    Args:
        dest_addr (String, optional): the 64-bit address of the solar panel to
            reset its position. If none is specified, all panels will be reset.
    """
    set_motor_position(DEFAULT_POS, dest_addr)
    print_log("Solar panel position reset ({})".format(dest_addr if dest_addr is not None else "ALL"))


def set_report_interval(interval):
    """
    Sets the new report interval.

    Args:
        interval (Integer): the new interval in seconds.
    """
    global report_interval

    # Save the new report interval.
    report_interval = interval

    data = list()

    data.append(CMD_ID_SET)
    data.append(1)
    data.append(ID_REPORT_INTERVAL)
    data.extend(list((interval * 1000).to_bytes(4, "big")))

    # Send the new interval to all solar devices.
    if send_data_xbee(bytearray(data)):
        print_log("Report interval changed to {} seconds.".format(interval))


def set_motor_position(position, dest_addr=None):
    """
    Sets the position of the solar panel with the given 64-bit address (or all
    if none is specified).
    The position must be between 90000 (90.0º) and 270000 (270.0º), or 0 to
    send an alarm.

    Args:
        position (Integer): the new position in degrees.
        dest_addr (String, optional): the 64-bit address of the solar panel to
            set its position. If none is specified, the position will be set to
            all panels.
    """
    if position != WIND_ALARM_POS and (position <= POSITION_MIN or position >= POSITION_MAX):
        return

    data = list()

    data.append(CMD_ID_SET)
    data.append(1)
    # Motor encoder position.
    data.append(SENS_ID_PANEL_POSITION)
    data.extend(list(position.to_bytes(4, "big")))

    # Send the new position to the specified device or to all.
    if send_data_xbee(bytearray(data), dest_addr):
        print_log("Motor position set to {} deg ({})".format(round(position / 1000),
                                                             dest_addr if dest_addr is not None else "ALL"))


def send_data_xbee(data, dest_addr=None):
    """
    Sends the given data to the solar device with the given 64-bit address. If
    none is provided, the data is sent to all panels.

    Args:
        data (Bytearray): the data to send.
        dest_addr (String, optional): the 64-bit address of the solar panel to
            send the data to. If none is specified, the data will be sent to
            all panels.

    Returns:
         ``True`` if the data could be sent successfully, ``False`` otherwise.
    """
    try:
        if dest_addr is None:
            device.send_data_broadcast(data)
        else:
            device.send_data(RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string(dest_addr)), data)
        return True
    except XBeeException:
        traceback.print_exc()

    return False


def get_sun_position():
    """
    Returns the current position of the sun based on the time of day.
    To simplify the demo as much as possible, only the solar elevation angle
    (the angle between the horizon and the centre of the sun's disc) is
    taken into account in the Earth's center (0º of latitude, 0º of longitude)
    and in the March equinox.
    It goes between 90000 (90.0º) at 6 am and 270000 (270º) at 6 pm.

    Returns:
        The current sun position in degrees * 1000.
    """
    time_now = datetime.now().time()
    time_d = time_now.hour + (time_now.minute / 60.0) + (time_now.second / 3600.0)

    position = round(time_d * 15000)
    if position < POSITION_MIN:
        position = POSITION_MIN
    elif position > POSITION_MAX:
        position = POSITION_MAX

    return position


def parse_configurations(payload):
    """
    Parses the configurations to perform from the given payload and returns a
    list containing tuples with the ID of the sensor to configure and the value
    to set.

    Args:
        payload (list): array of bytes to parse.

    Returns:
        A list containing tuples with the ID of the sensor to configure and the
        value to set.
    """
    # Initialize variables.
    index = 1
    configurations = []

    # Get the configurations from the payload.
    num_configurations = payload[index]
    index += 1
    for i in range(num_configurations):
        sensor_id = payload[index]
        index += 1
        value = int.from_bytes(bytearray(payload[index:index + 4]), "big")
        index += 4
        configurations.append((sensor_id, value))

    return configurations


def upload_configuration_drm(configuration, sender=None):
    """
    Uploads the given configuration to Digi Remote Manager.

    Args:
        configuration (tuple): the configuration to upload to DRM.
        sender (String, optional): the 64-bit address of the solar panel that
            originated the configuration. Use ``None`` if the configuration is
            from the solar controller.
    """
    sensor_id = configuration[0]
    sensor_value = configuration[1]

    # Generate the corresponding data stream.
    data_stream = DATA_STREAM_FORMAT.format(sender, sensor_id) if sender is not None else sensor_id
    # Upload the measurement as a new data point of the data stream.
    datapoint.upload(data_stream, sensor_value, data_type=datapoint.DataType.INT)


def get_next_random(value, max_value, min_value, max_delta):
    """
    Calculates and returns the next sensor value based on the current one, the
    limits and the maximum delta.

    Args:
        value (Integer): the current value of the sensor.
        max_value (Integer): the maximum value that the sensor can have.
        min_value (Integer): the minimum value that the sensor can have.
        max_delta (Integer): the maximum delta for the next value.

    Returns:
        The next sensor value based on the current one.
    """
    # Determine if sensor delta should be added or substracted.
    if value == max_value:
        add = False
    elif value == min_value:
        add = True
    else:
        add = random.random() > 0.5

    # Calculate a new delta.
    delta = random.randint(0, max_delta)

    # Apply the delta.
    if add:
        value += delta
    else:
        value -= delta
    if value > max_value:
        value = max_value
    elif value < min_value:
        value = min_value

    return value


def get_wind():
    """
    Returns the wind speed. The value is randomly calculated based on the
    current wind speed value.

    Returns:
        The new wind speed in km/h * 1000.
    """
    return get_next_random(wind, WIND_MAX, WIND_MIN, WIND_DELTA)


def get_light():
    """
    Returns the sun light. The value is randomly calculated based on the
    current sun light value.

    Returns:
        The new sun light in lx * 1000.
    """
    return get_next_random(light, LIGHT_MAX, LIGHT_MIN, LIGHT_DELTA)


def get_radiation():
    """
    Returns the sun irradiation. The value is randomly calculated based on the
    sun position.

    Returns:
        The new sun irradiation in W/m2 * 1000.
    """
    sun_pos = get_sun_position()
    if sun_pos <= POSITION_MIN or sun_pos >= POSITION_MAX:
        return 0
    else:
        sun_pos = sun_pos / 1000
        # Calculate a new delta.
        delta = random.randint(0, RADIATION_DELTA)
        if random.random() > 0.5:
            delta = -1 * delta
        # Calculate the radiation based on the sun position.
        new_radiation = round((-0.1279 * pow(sun_pos, 2) + 46.05 * sun_pos - 3100) * 1000)
        # Apply the delta and return the value.
        return new_radiation + delta


def get_runt(cmd):
    """
    Returns the response of the given runt command.

    Args:
        cmd (String): runt command to execute.

    Returns:
        The response of the given runt command.
    """
    runt.start()
    try:
        return runt.get(cmd)
    finally:
        runt.stop()


def print_log(msg):
    """
    Prints the given log message.

    Args:
        msg (string): log message to print.
    """
    print("[{}] {}".format(datetime.now(), msg))


def is_connected_drm():
    """
    Returns whether the device is connected to Digi Remote Manager or not.

    Returns:
        ``True`` if the device is connected to DRM, ``False`` otherwise.
    """
    return get_runt("drm.connected") == "true"


def wait_drm_connection():
    """
    Waits until the device is connected to Digi Remote Manager.
    """
    print_log("Waiting for connection with Digi Remote Manager...")
    # Check if the device is connected.
    while not is_connected_drm():
        time.sleep(10)
    # Check if the device has permissions in the registered account.
    while True:
        try:
            datapoint.upload("test", datetime.now())
            break
        except Exception:
            time.sleep(10)
    print_log("Device connected to Digi Remote Manager")


def configure_positions_task():
    """
    Timer task to configure the positions of all the solar panels.
    """
    position = get_sun_position()
    new_wind = get_wind()

    # If the wind speed is above the threshold, send an alarm to the solar panels.
    if new_wind >= WIND_THRESHOLD:
        set_motor_position(WIND_ALARM_POS)
    else:
        for dev in auto_follow_dict:
            if auto_follow_dict[dev]:
                set_motor_position(position, dev)

    # Create and start a timer to repeat this task periodically.
    Timer(POSITIONS_INTERVAL, configure_positions_task).start()


def drm_report_task():
    """
    Timer task to send the sensors report to Digi Remote Manager.
    """
    global wind, light, radiation
    configurations = list()

    print_log("Sending sensor values to DRM:")

    # Obtain the values from the sensors.
    wind = get_wind()
    print_log("  - Wind: {} km/h".format(round(wind / 1000)))

    light = get_light()
    print_log("  - Light: {} lx".format(round(light / 1000)))

    radiation = get_radiation()
    print_log("  - Radiation: {} W/m2".format(round(radiation / 1000)))

    configurations.append((SENS_ID_CONT_WIND, wind))
    configurations.append((SENS_ID_CONT_LIGHT, light))
    configurations.append((SENS_ID_CONT_RADIATION, radiation))

    for configuration in configurations:
        upload_configuration_drm(configuration)

    # Create and start a timer to repeat this task periodically.
    Timer(report_interval, drm_report_task).start()


def main():
    """
    Main execution of the application.
    """

    print(" +-----------------------------+")
    print(" | End-to-End IoT Solar Sample |")
    print(" +-----------------------------+\n")

    global device
    device = xbee.get_device()

    # Open the connection with the XBee device.
    device.open()
    device.set_api_output_mode(APIOutputMode.EXPLICIT)

    # Register a callback to handle incoming data from the Bluetooth interface.
    device.add_bluetooth_data_received_callback(bluetooth_data_callback)

    # Wait until the controller is connect to Digi Remote Manager.
    wait_drm_connection()

    # Register callbacks to handle incoming data from Digi Remote Manager.
    device_request.register(DRM_TARGET_AUTO_FOLLOW, drm_request_callback)
    device_request.register(DRM_TARGET_RESET_POSITION, drm_request_callback)
    device_request.register(DRM_TARGET_SAMPLING_RATE, drm_request_callback)

    # Register a callback to handle incoming data from any XBee device of the network.
    device.add_data_received_callback(xbee_data_callback)

    # Register a callback to handle incoming packets from any XBee device of the network.
    device.add_packet_received_callback(xbee_packet_callback)

    # Start the task to configure the solar panels positions.
    configure_positions_task()

    # Start the task to report the sensor values to DRM (only if this is the main controller).
    if is_main_controller():
        drm_report_task()


if __name__ == '__main__':
    main()
