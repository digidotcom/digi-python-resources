# Copyright (c) 2020, 2021, Digi International, Inc.
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
import signal
import sys
import time
from datetime import datetime
from json import JSONDecodeError
from threading import Thread, Timer, Event, Lock
import serial

from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.exception import XBeeException
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.packets.aft import ApiFrameType
from digi.xbee.util import utils
from digidevice import config, datapoint, device_request, runt, xbee
from digidevice.datapoint import DataType

# Constants.
DRM_TARGET_SET_AUTO_IRRIGATION = "set_auto_irrigation"
DRM_TARGET_SET_TANK_VALVE = "set_tank_valve"
DRM_TARGET_SET_STATION_VALVE = "set_station_valve"
DRM_TARGET_SET_SAMPLING_RATE = "set_sampling_rate"
DRM_TARGET_GET_CONDITION = "get_condition"
DRM_TARGET_SET_CONDITION = "set_condition"
DRM_TARGET_GET_TIME = "get_time"
DRM_TARGET_GET_TIME_FACTOR = "get_time_factor"
DRM_TARGET_SET_TIME_FACTOR = "set_time_factor"
DRM_TARGET_GET_SCHEDULE = "get_schedule"
DRM_TARGET_SET_SCHEDULE = "set_schedule"
DRM_TARGET_REFILL_TANK = "refill_tank"
DRM_TARGET_IS_MAIN_CONTROLLER = "is_main_controller"

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
PROP_SCHEDULE = "schedule"
PROP_START_TIME = "start_time"
PROP_DURATION = "duration"

STAT_TIME = "time"
STAT_TIME_FACTOR = "time_factor"
STAT_CONDITION = "condition"
STAT_VALVE = "valve"
STAT_TEMPERATURE = "temperature"
STAT_MOISTURE = "moisture"
STAT_PRESSURE = "pressure"
STAT_LUMINOSITY = "luminosity"
STAT_BATTERY = "battery"
STAT_RAIN = "rain"
STAT_WIND = "wind_speed"
STAT_WIND_DIR = "wind_direction"
STAT_RADIATION = "radiation"
STAT_LEVEL = "level"

OP_ID = "id"
OP_READ = "read"
OP_WRITE = "write"
OP_FINISH = "finish"
OP_STATUS = "status"

STATUS_SUCCESS = "success"
STATUS_ERROR = "error"

VALUE_ID = "controller"

FILE_PROPERTIES = "./properties.txt"

POSITION_MAX = 270  # 270º
POSITION_MIN = 90   # 90º

WIND_MAX = 120  # 120 km/h
WIND_MIN = 0    # 0 km/h
WIND_DELTA = 2  # 2 km/h

RADIATION_DELTA = 10  # 10 W/m2

DEFAULT_TEMP = 23               # 23 ºC
DEFAULT_MOIST = 50                # 50 %
DEFAULT_PRES = 25               # 27 hPa
DEFAULT_RAIN = 0                # 0 mm
DEFAULT_WIND = 5                # 5 km/h
DEFAULT_WIND_DIR = "N"          # N (North)
DEFAULT_LUM = 50         # 50 %
DEFAULT_RADIATION = 350         # 350 W/m2
DEFAULT_TANK_LEVEL = 50         # 50 %
DEFAULT_VALVE_POSITION = False  # Closed
DEFAULT_IRR_DURATION = 600      # 10 minutes
DEFAULT_REPORT_INTERVAL = 60    # 1 minute

TANK_DRAIN_RATE = 0.001  # 0.001 % / second

TANK_LEVEL_THRESHOLD = 10  # 10 %
MOISTURE_THRESHOLD = 60    # 60 %

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

CONDITION_SUNNY = 0
CONDITION_CLOUDY = 1
CONDITION_RAINY = 2

SECONDS_PER_DAY = 24 * 60 * 60

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

DATA_SEPARATOR = "@@"
PROP_FW_VERSION = "firmware.version"

OLD_FW_YEAR = 21
OLD_FW_MONTH = 8

# Variables.
device = None

start_sending_data = False

current_time = 0
time_factor = 1
weather_condition = CONDITION_SUNNY

temp = DEFAULT_TEMP
moist = DEFAULT_MOIST
pres = DEFAULT_PRES
rain = DEFAULT_RAIN
wind = DEFAULT_WIND
wind_dir = DEFAULT_WIND_DIR
luminosity = DEFAULT_LUM
radiation = DEFAULT_RADIATION
tank_level = DEFAULT_TANK_LEVEL
tank_valve_open = DEFAULT_VALVE_POSITION
report_interval = DEFAULT_REPORT_INTERVAL

auto_irrigation = True
is_irrigating = False

auto_irrigation_dict = dict()
station_valve_dict = dict()
station_moisture_dict = dict()

irrigation_schedule = []

event = Event()

datapoint_lock = Lock()


# TODO: Replace with the serial port used to receive data.
PORT = "/dev/serial/port1"
# TODO: Replace with the preferred baud rate.
BAUD_RATE = 9600

# Optional serial settings
STOP_BITS = serial.STOPBITS_ONE
N_DATA_BITS = 8
PARITY = serial.PARITY_NONE
RTS_CTS = 0


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
            response[ITEM_MSG] = "Error writing properties in the XBee module."
    elif operation == OP_FINISH:
        finish_provisioning()
        return
    else:
        return

    # Send back the response.
    device.send_bluetooth_data(json.dumps(response).encode())


def drm_request_callback(target, request):
    """
    Callback executed every time the irrigation controller receives a device
    request from Digi Remote Manager.
    Processes the incoming request depending on the target and executes the
    corresponding action.

    Args:
        target (String): the device request target.
        request (String): the device request.
    """
    global report_interval, weather_condition, time_factor, tank_level

    data = request.strip()

    # Execute the corresponding action based on the target.
    if target == DRM_TARGET_SET_AUTO_IRRIGATION:
        data, dest_addr = get_data_address(request)
        set_auto_irrigation(data == "1", dest_addr)
    elif target == DRM_TARGET_SET_TANK_VALVE:
        return set_tank_valve(data == "1")
    elif target == DRM_TARGET_SET_STATION_VALVE:
        data, dest_addr = get_data_address(request)
        return set_station_valve(data == "1", dest_addr)
    elif target == DRM_TARGET_SET_SAMPLING_RATE:
        report_interval = int(data)
        print_log("Report interval changed to {} seconds".format(report_interval))
    elif target == DRM_TARGET_GET_CONDITION:
        return str(weather_condition)
    elif target == DRM_TARGET_SET_CONDITION:
        set_weather_condition(int(data))
    elif target == DRM_TARGET_GET_TIME:
        return str(current_time)
    elif target == DRM_TARGET_GET_TIME_FACTOR:
        return str(time_factor)
    elif target == DRM_TARGET_SET_TIME_FACTOR:
        time_factor = int(data)
        print_log("Time factor changed to {}".format(time_factor))
    elif target == DRM_TARGET_GET_SCHEDULE:
        return get_irrigation_schedule()
    elif target == DRM_TARGET_SET_SCHEDULE:
        set_irrigation_schedule(data)
    elif target == DRM_TARGET_REFILL_TANK:
        return refill_tank()
    elif target == DRM_TARGET_IS_MAIN_CONTROLLER:
        return is_main_controller()


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

    # Parse the received JSON.
    try:
        json_items = json.loads(msg.data.decode())
    except (JSONDecodeError, UnicodeDecodeError):
        return

    # If the sender is not in the auto-irrigation dictionary, add it with the default value.
    if sender not in auto_irrigation_dict:
        auto_irrigation_dict[sender] = auto_irrigation

    if msg.is_broadcast or json_items[ITEM_OP] != OP_STATUS:
        return

    print_log("Sensor data received from '{}' with payload '{}'".format(sender, msg.data.decode()))

    properties = json_items[ITEM_PROP]

    # Update the valve position and last moisture in the dictionaries.
    if STAT_VALVE in properties:
        station_valve_dict[sender] = True if properties[STAT_VALVE] == 1 else False
    if STAT_MOISTURE in properties:
        station_moisture_dict[sender] = float(properties[STAT_MOISTURE])

    # Parse the configurations contained in the message and upload them to DRM.
    upload_configurations_drm(parse_configurations(properties), sender)


def xbee_packet_callback(packet):
    """
    Callback executed every time the XBee device receives an XBee packet.
    The irrigation stations send a packet every time they join to the XBee
    network, so this method processes those packets in order to keep the list
    of remote devices up to date.

    Args:
        packet (:class:`XBeeAPIPacket`): the packet received.
    """
    if packet.get_frame_type() == ApiFrameType.EXPLICIT_RX_INDICATOR:
        sender = str(packet.x64bit_source_addr)
        # If the sender is not in the auto-irrigation dictionary, add it with the default value.
        if sender not in auto_irrigation_dict:
            auto_irrigation_dict[sender] = auto_irrigation


def signal_handler(signal_number, _frame):
    """
    Signal handler function.

    Args:
        signal_number (Integer): Received signal.
        _frame: Current stack frame.
    """
    if signal_number in (signal.SIGTERM, signal.SIGINT, signal.SIGQUIT):
        event.set()


def get_data_address(request):
    """
    Returns the data and the address (if contained) of the given request.

    Args:
        request (String): the request.

    Returns:
        The data and the address (None if no address is contained) of the
        request.
    """
    # Check if the request is for a specific station or for all.
    if len(request) >= MIN_DRM_REQUEST_ADDR_SIZE:
        data_values = request.split(DATA_SEPARATOR)
        dest_addr = data_values[0].strip()
        data = data_values[1].strip()
        return data, dest_addr
    return request, None


def save_properties(properties):
    """
    Saves the given properties in the XBee firmware of the device.

    Args:
        properties (dict): dictionary containing the properties to save.

    Returns:
        ``True`` if the properties were saved successfully, ``False``
        otherwise.
    """
    # Save XBee properties in the XBee firmware.
    try:
        for prop in XBEE_PROPERTIES:
            # Skip empty properties.txt.
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
        print_error("Could not save properties in the XBee firmware: {}".format(str(e)))

    return False


def write_xbee_settings():
    """
    Applies and writes the configured XBee properties.txt.
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
    # If the properties file does not exist, create it first.
    if not os.path.exists(FILE_PROPERTIES):
        open(FILE_PROPERTIES, "x").close()

    # Read the file contents and parse the JSON.
    f = open(FILE_PROPERTIES, "r")
    try:
        data = json.loads(f.read())
    except JSONDecodeError:
        data = {}
    finally:
        f.close()

    # Set the new status.
    data[PROP_MAIN_CONTROLLER] = is_main

    # Write the file.
    f = open(FILE_PROPERTIES, "w")
    f.write(json.dumps(data))
    f.close()


def is_main_controller():
    """
    Returns whether this is the main controller or not.

    Returns:
        ``True`` if this is the main controller, ``False`` otherwise.
    """
    # If the properties file exists, read it.
    if os.path.exists(FILE_PROPERTIES):
        f = open(FILE_PROPERTIES)
        try:
            data = json.loads(f.read())
        except JSONDecodeError:
            data = {}
        finally:
            f.close()
        if PROP_MAIN_CONTROLLER in data and data[PROP_MAIN_CONTROLLER]:
            return True
    return False


def finish_provisioning():
    """
    Finishes the provisioning phase by disabling the Bluetooth interface.
    """
    # Disable the Bluetooth interface.
    cfg = config.load(writable=True)
    cfg.set("bluetooth.enable", False)
    cfg.commit()


def set_auto_irrigation(irrigate, dest_addr=None):
    """
    Sets whether the irrigation station with the given address (or all if none
    is specified) should irrigate automatically or not.

    Args:
        irrigate (Boolean): ``True`` to auto-irrigate, ``False`` otherwise.
        dest_addr (String, optional): the 64-bit address of the station the
            auto-irrigate property will be applied to. If none is specified, it
            will be applied to all stations.
    """
    global auto_irrigation

    # Update the value in the dictionary.
    if dest_addr is not None:
        auto_irrigation_dict[dest_addr] = irrigate
    else:
        auto_irrigation = irrigate
        for dev in auto_irrigation_dict:
            auto_irrigation_dict[dev] = irrigate

    print_log("Auto-irrigation {} ({})".format("enabled" if irrigate else "disabled",
                                               dest_addr if dest_addr is not None else "ALL"))


def start_irrigation(duration=DEFAULT_IRR_DURATION):
    """
    Starts the irrigation process.

    Args:
        duration (Integer, optional): duration in seconds of the irrigation
            process for each station.
    """
    global is_irrigating

    if tank_level == 0:
        print_log("ERROR: could not start the irrigation process, the tank is empty")
        return

    is_irrigating = True
    print_log("Irrigation process started for {} seconds".format(duration))

    # Open the tank valve.
    set_tank_valve(True)

    for dev in auto_irrigation_dict:
        # Start the irrigation in the given station only if it has the auto-irrigation enabled
        # and the current moisture is under the threshold.
        if auto_irrigation_dict[dev] and station_moisture_dict[dev] < MOISTURE_THRESHOLD:
            # Open the station valve.
            set_station_valve(True, dev)
            # Wait during the configured time.
            start_time = current_time
            while current_time < start_time + duration:
                # If the tank is empty, do not continue.
                if tank_level == 0:
                    print_log("WARNING: irrigation process stopped, the tank is empty")
                    break
                time.sleep(0.5)
            # Close the station valve.
            set_station_valve(False, dev)
            # If the tank is empty, do not continue.
            if tank_level == 0:
                break

    # Close the tank valve.
    set_tank_valve(False)

    is_irrigating = False
    print_log("Irrigation process finished")


def set_tank_valve(is_open):
    """
    Sets the valve position of the tank.

    Args:
        is_open (Boolean): ``True`` to open the valve, ``False`` to close it.

    Returns:
        The new position of the tank valve.
    """
    global tank_valve_open

    tank_valve_open = is_open

    # Upload a datapoint with the new position.
    Thread(target=upload_configurations_drm, args=([(STAT_VALVE, int(is_open))],), daemon=True).start()

    print_log("Tank valve is now {}".format("open" if tank_valve_open else "closed"))
    return AT_VALUE_ENABLED if is_open else AT_VALUE_DISABLED


def set_station_valve(is_open, dest_addr=None):
    """
    Sets the valve position of the station with the given 64-bit address (or of
    all stations if none is specified).

    Args:
        is_open (Boolean): ``True`` to open the valve, ``False`` to close it.
        dest_addr (String, optional): the 64-bit address of the station to
            set the valve position. If none is specified, it applies to all
            stations.

    Returns:
        The new position of the station valve.
    """
    # Update the valve position in the dictionary.
    if dest_addr is not None:
        station_valve_dict[dest_addr] = is_open
    else:
        for dev in station_valve_dict:
            station_valve_dict[dev] = is_open

    # Send the new valve position to the specified station or to all.
    if send_status_request([(STAT_VALVE, int(is_open))], dest_addr):
        print_log("Station valve is now {} ({})".format("open" if is_open else "closed",
                                                        dest_addr if dest_addr is not None else "ALL"))
        return AT_VALUE_ENABLED if is_open else AT_VALUE_DISABLED
    return ""


def any_open_valve():
    """
    Returns whether there is any station valve open or not.

    Returns:
        ``True`` if there is any station valve open, ``False`` otherwise.
    """
    for dev in station_valve_dict:
        if station_valve_dict[dev]:
            return True
    return False


def set_weather_condition(condition):
    """
    Sets the new weather condition.

    Args:
        condition (Integer): the new weather condition.
    """
    global weather_condition

    weather_condition = condition

    # Send the new weather condition to all stations.
    if send_status_request([(STAT_CONDITION, weather_condition)]):
        print_log("Condition changed to {}".format(weather_condition))


def load_irrigation_schedule():
    """
    Loads the irrigation schedule from the properties file.
    """
    global irrigation_schedule

    # Read and parse the properties file.
    if not os.path.exists(FILE_PROPERTIES):
        return

    f = open(FILE_PROPERTIES)
    try:
        data = json.loads(f.read())
    except JSONDecodeError:
        data = {}
    finally:
        f.close()

    if PROP_SCHEDULE in data:
        irrigation_schedule = data[PROP_SCHEDULE]


def get_irrigation_schedule():
    """
    Returns the irrigation schedule in JSON format.

    Returns:
        The irrigation schedule in JSON format.
    """
    schedule = {PROP_SCHEDULE: irrigation_schedule}
    return json.dumps(schedule)


def set_irrigation_schedule(schedule):
    """
    Sets the new irrigation schedule.

    Args:
        schedule (String): the new schedule in JSON format.
    """
    global irrigation_schedule

    # Read and parse the properties file.
    f = open(FILE_PROPERTIES)
    try:
        data = json.loads(f.read())
    except JSONDecodeError:
        data = {}
    finally:
        f.close()

    # Parse the given schedule.
    try:
        sch_json = json.loads(schedule)
    except JSONDecodeError:
        sch_json = {}

    data[PROP_SCHEDULE] = sch_json[PROP_SCHEDULE]

    # Write the file with the new schedule.
    f = open(FILE_PROPERTIES, "w")
    f.write(json.dumps(data))
    f.close()

    irrigation_schedule = data[PROP_SCHEDULE]

    print_log("Changed the irrigation schedule: {}".format(irrigation_schedule))


def refill_tank():
    """
    Refills the tank to 100%.

    Returns:
        The new tank level.
    """
    global tank_level

    tank_level = 100

    # Upload a datapoint with the new level.
    Thread(target=upload_configurations_drm, args=([(STAT_LEVEL, tank_level)],), daemon=True).start()

    print_log("Tank refilled")
    return tank_level


def send_status_request(props, dest_addr=None):
    """
    Sends the status request with the given properties to the station with the
    given 64-bit address.

    Args:
        props (List): list of properties to send.
        dest_addr (String, optional): the 64-bit address of the station to
            send the status. If none is specified, it is sent to all stations.

    Returns:
        ``True`` if the request could be sent successfully, ``False`` otherwise.
    """
    request = {}
    properties = {}

    request[ITEM_OP] = OP_STATUS

    for prop in props:
        properties[prop[0]] = prop[1]

    request[ITEM_PROP] = properties

    return send_data_xbee(json.dumps(request).encode(), dest_addr)


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
    except XBeeException as e:
        print_error("Could not send data: {}".format(str(e)))

    return False


def get_sun_position():
    """
    Returns the current position of the sun based on the time of day.
    To simplify the demo as much as possible, only the solar elevation angle
    (the angle between the horizon and the centre of the sun's disc) is
    taken into account in the Earth's center (0º of latitude, 0º of longitude)
    and in the March equinox.
    It goes between 90º at 6 am and 270º at 6 pm.

    Returns:
        The current sun position in degrees.
    """
    time_now = datetime.now().time()
    time_d = time_now.hour + (time_now.minute / 60.0) + (time_now.second / 3600.0)

    position = round(time_d * 15)
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
    configurations = []

    for conf in payload:
        configurations.append((conf, payload[conf]))

    return configurations


def upload_configurations_drm(configurations, sender=None):
    """
    Uploads the given configurations to Digi Remote Manager.
    Args:
        configurations (list of tuple): the configurations to upload to DRM.
        sender (String, optional): the 64-bit address of the solar panel that
            originated the configuration. Use ``None`` if the configuration is
            from the solar controller.
    """
    # Check if multiple data point upload can be used
    if is_old_firmware():
        for config in configurations:
            conf_id = config[0]
            conf_value = config[1]

            # Generate the corresponding data stream.
            data_stream = DATA_STREAM_FORMAT.format(sender, conf_id) if sender is not None else conf_id
            # Upload the measurement as a new data point of the data stream.
            try:
                with datapoint_lock:
                    datapoint.upload(data_stream, conf_value, data_type=datapoint.DataType.DOUBLE)
            except Exception as e:
                print_error("Could not upload datapoint to stream '{}': {}".format(data_stream, str(e)))
    else:
        from digidevice.datapoint import DataPoint
        data_points = []
        for config in configurations:
            conf_id = config[0]
            conf_value = config[1]

            # Generate the corresponding data stream.
            data_stream = DATA_STREAM_FORMAT.format(sender, conf_id) if sender is not None else conf_id
            # Create and store the data point.
            data_points.append(DataPoint(data_stream, conf_value, data_type=DataType.DOUBLE))

            # Upload the data points all at once.
            try:
                with datapoint_lock:
                    datapoint.upload_multiple(data_points)
            except Exception as e:
                print_error("Could not upload datapoints: {}".format(str(e)))


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


def get_temp():
    """
    Returns the temperature. The value is obtained from the
    meteo station.

    Returns:
        The new temperature in ºC.
    """
    return temp


def get_rain(simulation=False):
    """
    Returns the rain during the day. The value is randomly calculate based on
    the current weather condition.

    Returns:
        The rain in mm.
    """
    rain_var = 0

    if simulation:
        # Report rain only if the condition is 'rainy' (and not always).
        if weather_condition == CONDITION_RAINY and random.random() > 0.7:
            rain_var += round(random.random(), 2)

    else:
        rain_var = rain

    # Conversion from inch to mm
    return rain_var * 25.4


def get_wind(simulation=False):
    """
    Returns the wind speed. If simulation is set to True, the value is randomly
    calculated based on the current wind speed value.
    If it is set to False, then the value is obtained from the meteo station.

    Returns:
        The new wind speed in km/h.
    """

    if simulation:
        return get_next_random(wind, WIND_MAX, WIND_MIN, WIND_DELTA)
    else:
        # Conversion from miles/h to km/h
        return round(wind * 1.609, 1)


def get_moist():
    """
    Returns the moisture/humidity of the air. The value is obtained from the
    meteo station.

    Returns:
        The new moisture in %.
    """
    return moist


def get_pres():
    """
    Returns the pressure of the air. The value is obtained from the
    meteo station.

    Returns:
        The new pressure in hPa.
    """
    return pres


def get_wind_dir():
    """
    Returns the wind direction. The value is obtained from the
    meteo station.

    Returns:
        The new wind direction in compass values.
    """

    return wind_dir


def get_luminosity():
    """
    Returns the luminosity. The value is obtained from the
    meteo station.

    Returns:
        The new luminosity in lux.
    """

    # Original value from 0 to 255
    return luminosity * 10000 / 255


def get_radiation():
    """
    Returns the sun irradiation. The value is randomly calculated based on the
    sun position.

    Returns:
        The new sun irradiation in W/m2.
    """
    sun_pos = get_sun_position()
    if sun_pos <= POSITION_MIN or sun_pos >= POSITION_MAX:
        return 0
    else:
        # Calculate a new delta.
        delta = random.randint(0, RADIATION_DELTA)
        if random.random() > 0.5:
            delta = -1 * delta
        # Calculate the radiation based on the sun position.
        new_radiation = round(-0.1279 * pow(sun_pos, 2) + 46.05 * sun_pos - 3100)
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


def print_error(msg):
    """
    Prints the given error message.

    Args:
        msg (string): error message to print.
    """
    print("[{}] {}".format(datetime.now(), msg), file=sys.stderr)


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


def register_drm_targets():
    """
    Register all the Digi Remote Manager targets.
    """
    device_request.register(DRM_TARGET_SET_AUTO_IRRIGATION, drm_request_callback)
    device_request.register(DRM_TARGET_SET_TANK_VALVE, drm_request_callback)
    device_request.register(DRM_TARGET_SET_STATION_VALVE, drm_request_callback)
    device_request.register(DRM_TARGET_SET_SAMPLING_RATE, drm_request_callback)
    device_request.register(DRM_TARGET_GET_CONDITION, drm_request_callback)
    device_request.register(DRM_TARGET_SET_CONDITION, drm_request_callback)
    device_request.register(DRM_TARGET_GET_TIME, drm_request_callback)
    device_request.register(DRM_TARGET_GET_TIME_FACTOR, drm_request_callback)
    device_request.register(DRM_TARGET_SET_TIME_FACTOR, drm_request_callback)
    device_request.register(DRM_TARGET_GET_SCHEDULE, drm_request_callback)
    device_request.register(DRM_TARGET_SET_SCHEDULE, drm_request_callback)
    device_request.register(DRM_TARGET_REFILL_TANK, drm_request_callback)
    device_request.register(DRM_TARGET_IS_MAIN_CONTROLLER, drm_request_callback)


def drm_report_task():
    """
    Timer task to send the sensors report to Digi Remote Manager.
    """
    configurations = list()

    if start_sending_data:

        print_log("Sending sensor values to DRM:")

        # Obtain the values from the sensors.
        temp_calc = get_temp()
        print_log("  - Temp: {} C".format(temp_calc))

        moist_calc = get_moist()
        print_log("  - Moist: {} %".format(moist_calc))

        pres_calc = get_pres()
        print_log("  - Pres: {} hPa".format(pres_calc))

        rain_calc = get_rain()
        rain_f = "{:.2f}".format(rain_calc)
        print_log("  - Rain: {} mm".format(rain_f))

        wind_calc = get_wind()
        print_log("  - Wind: {} km/h".format(wind_calc))

        wind_dir_calc = get_wind_dir()
        wind_dir_degrees = 0
        if wind_dir_calc == "N":
            wind_dir_degrees = 0
        elif wind_dir_calc == "E":
            wind_dir_degrees = 16
        elif wind_dir_calc == "S":
            wind_dir_degrees = 32
        elif wind_dir_calc == "W":
            wind_dir_degrees = 48
        elif wind_dir_calc == "NE":
            wind_dir_degrees = 8
        elif wind_dir_calc == "NW":
            wind_dir_degrees = 56
        elif wind_dir_calc == "SE":
            wind_dir_degrees = 24
        else:
            wind_dir_degrees = 40

        print_log("  - Wind dir: {} ({})".format(wind_dir, wind_dir_degrees))

        luminosity_calc = get_luminosity()
        luminosity_f = "{:.2f}".format(luminosity_calc)
        print_log("  - Luminosity: {} lux".format(luminosity_f))

        radiation_calc = get_radiation()
        print_log("  - Radiation: {} W/m2".format(radiation_calc))

        tank_level_f = "{:.3f}".format(tank_level)
        print_log("  - Tank level: {} %".format(tank_level_f))

        print_log("  - Tank valve: {}".format("open" if tank_valve_open else "closed"))
        print_log("")

        configurations.append((STAT_TEMPERATURE, temp_calc))
        configurations.append((STAT_MOISTURE, moist_calc))
        configurations.append((STAT_PRESSURE, pres_calc))
        configurations.append((STAT_RAIN, rain_f))
        configurations.append((STAT_WIND, wind_calc))
        configurations.append((STAT_WIND_DIR, wind_dir_degrees))
        configurations.append((STAT_LUMINOSITY, luminosity_f))
        configurations.append((STAT_RADIATION, radiation_calc))
        configurations.append((STAT_LEVEL, tank_level_f))
        configurations.append((STAT_VALVE, int(tank_valve_open)))

        upload_configurations_drm(configurations)

    # Create and start a timer to repeat this task periodically.
    t = Timer(report_interval, drm_report_task)
    t.setDaemon(True)
    t.start()


def status_task():
    """
    Timer to task to request the status from the irrigation stations.
    """
    props = [
        (STAT_TIME, current_time),
        (STAT_CONDITION, weather_condition)
    ]

    # Send the status request with the current time and condition.
    send_status_request(props)

    # Create and start a timer to repeat this task periodically.
    t = Timer(report_interval, status_task)
    t.setDaemon(True)
    t.start()


def time_task():
    """
    Timer task to control the actions that take place every second:
      - Increase the time based on the configured time factor.
      - Reset the rain accumulate at midnight.
      - Update the tank level based on the position of the valves.
      - Start the irrigation process.
    """
    global current_time, rain, tank_level

    while True:
        start_time = time.time()

        # Reset the rain at midnight.
        if (current_time + time_factor) // SECONDS_PER_DAY > 0:
            rain = 0

        # Update the tank level based on the tank & station valves.
        if tank_valve_open and any_open_valve():
            delta = time_factor * TANK_DRAIN_RATE
            if tank_level - delta < 0:
                tank_level = 0
            else:
                tank_level -= delta

        # Check if the irrigation process has to start.
        for sch in irrigation_schedule:
            if current_time < int(sch[PROP_START_TIME]) <= current_time + time_factor and not is_irrigating:
                Thread(target=start_irrigation, args=(int(sch[PROP_DURATION]),), daemon=True).start()

        # Increase the current time.
        current_time = (current_time + time_factor) % SECONDS_PER_DAY

        # Sleep the appropriate time so that this task is repeated exactly every 1 second.
        time.sleep(1.0 - (time.time() - start_time))


def is_old_firmware():
    """
    Returns whether the firmware running is an old version or not in
    terms of data point upload capabilities.
    Returns:
        Boolean: ``True`` if the device firmware is old, ``False`` otherwise.
    """
    # Read firmware version from runt.
    fw_version = get_runt(PROP_FW_VERSION)

    # Compare firmware year and month with old versions.
    year = int(fw_version.split(".")[0])
    month = int(fw_version.split(".")[1])
    if year < OLD_FW_YEAR:
        return True
    if year == OLD_FW_YEAR:
        if month < OLD_FW_MONTH:
            return True

    return False


def microbit_data(data):
    """
    Data obtained from the measurement made by the micro:bit application
    using a meteorologic station.
    Processes the incoming data in JSON format and assigns values to
    the program variables.

    Args
        data (Bytearray): the received data.
    """

    # Parse the JSON measurement items
    try:
        meas_items = json.loads(data.decode())
    except JSONDecodeError:
        return

    global temp, moist, pres, rain, wind, wind_dir, luminosity

    temp = meas_items["temp"]
    moist = meas_items["hum"]
    pres = meas_items["pres"]
    rain = meas_items["rain"]
    wind = meas_items["current_windSpeed"]
    wind_dir = meas_items["current_windDirection_List"]
    luminosity = meas_items["lightVal"]

    # meas_data = [temp, moist, pres, rain, wind, wind_dir, luminosity]
    # return meas_data


def read_microbit():
    """
    Reading of the meteo station data with the microbit application

    Returns:
        Data collected.
    """

    global start_sending_data

    # Create and configure the serial port settings
    ser = serial.Serial()
    ser.baudrate = BAUD_RATE
    ser.port = PORT
    ser.stopbits = STOP_BITS
    ser.bytesize = N_DATA_BITS
    ser.parity = PARITY
    ser.rtscts = RTS_CTS
    data = ""

    # Open the serial port
    ser.open()

    try:
        while True:
            if ser.in_waiting:
                data = ser.read(ser.in_waiting)
                microbit_data(data)
                start_sending_data = True
            time.sleep(1)

    except KeyboardInterrupt:
        # Close the serial port
        ser.close()

    return data


def main():
    """
    Main execution of the application.
    """

    print(" +-----------------------------------+")
    print(" | End-to-End IoT Agriculture Sample |")
    print(" +-----------------------------------+\n")

    global device, current_time

    # Register callbacks for signals processing.
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGQUIT, signal_handler)

    # Get the XBee device and open the connection.
    device = xbee.get_device()
    device.open()

    # Register a callback to handle incoming data from the Bluetooth interface.
    device.add_bluetooth_data_received_callback(bluetooth_data_callback)

    # Wait until the controller is connect to Digi Remote Manager.
    wait_drm_connection()

    # Register callbacks to handle incoming data from Digi Remote Manager.
    register_drm_targets()

    # Register a callback to handle incoming data from any XBee device of the network.
    device.add_data_received_callback(xbee_data_callback)

    # Register a callback to handle incoming packets from any XBee device of the network.
    device.add_packet_received_callback(xbee_packet_callback)

    # Load the irrigation schedule from the properties file.
    load_irrigation_schedule()

    # Reads the values from the microbit application connected to the meteo station
    # and sets this data to be sent to DRM
    Thread(target=read_microbit, daemon=True).start()

    # Start a task to move the time based on the factor.
    time_now = datetime.now().time()
    current_time = (time_now.hour * 3600) + (time_now.minute * 60) + time_now.second
    Thread(target=time_task, daemon=True).start()

    # Start a task to get the status from the irrigation stations.
    status_task()

    # TODO: Remove for final version as main controller is set in the provisioning step.
    set_main_controller(True)

    # Start the task to report the sensor values to DRM (only if this is the main controller).

    if is_main_controller():
        drm_report_task()

    event.wait()


if __name__ == '__main__':
    main()

