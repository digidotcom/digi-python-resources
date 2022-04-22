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
import argparse
import json
import logging
import os
import signal
import sys
import time
from enum import Enum
from logging.handlers import SysLogHandler
from threading import Thread, Event

from digidevice import device_request, xbee

from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.exception import XBeeException
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.models.protocol import Role
from digi.xbee.profile import ProfileUpdateTask


APP_NAME = "DRM XBee Network Update"

# Variables.
stop_event = Event()
log = logging.getLogger(APP_NAME)


class UpdateType(Enum):
    """
    This class lists DRM update types.
    """
    NODE = (0, "node")
    ROLE = (1, "role")
    GROUP = (2, "group")

    def __init__(self, code, desc):
        self._code = code
        self._desc = desc

    @property
    def code(self):
        """
        Returns the code of the `UpdateType` element.

        Returns:
            Integer: Code of the `UpdateType` element.
        """
        return self._code

    @property
    def desc(self):
        """
        Returns the description of the `UpdateType` element.

        Returns:
            String: Description of the `UpdateType` element.
        """
        return self._desc

    @classmethod
    def get(cls, code):
        """
        Returns the update type for the given code.

        Args:
            code (Integer): Code of the update type to get.

        Returns:
            :class:`.UpdateType`: Update type with the given code, `None` if not found.
        """
        for update_type in cls:
            if code == update_type.code:
                return update_type
        return None


class UpdateRequest:
    """
    Class to perform XBee update tasks.
    """

    _PROFILE_PATH = "/etc/config/xbee-profiles"

    _GROUP_SEPARATOR = ","

    _INVALID_REQUEST_ERROR = "Invalid request"
    _INVALID_TASK_ERROR = "Invalid update task"

    def __init__(self, request, ignore_invalid_tasks=False):
        """
        Class constructor. Instantiates a new :class:`.UpdateRequest`.

        Args:
            request (String or bytearray): Request to parse.
            ignore_invalid_tasks (Boolean, optional, default=`False`): `False`
                to raise a `ValueError` exception if any task in a request is
                not properly defined. `True` to ignore malformed tasks.

        Raises:
            ValueError: If the request is invalid.
        """
        if isinstance(request, (bytearray, bytes)):
            self._request = request.decode(encoding="utf-8").strip()
        elif isinstance(request, str):
            self._request = request.strip()
        else:
            raise ValueError(f"{self._INVALID_REQUEST_ERROR}: must be a string or bytearray")

        self._ignore_invalid_tasks = ignore_invalid_tasks
        self._update_tasks = {}
        self._parse_request()

        if not self._update_tasks:
            raise ValueError(f"{self._INVALID_REQUEST_ERROR} '{self._request}'")

    @property
    def tasks(self):
        """
        Returns the parsed update tasks from the request.

        Returns:
             Dictionary: As key a :class::`.XBee64BitAddress` or a
                :class::`.Role` and as value a tuple with profile path as
                string and the timeout as integer.
        """
        return self._update_tasks

    @property
    def request_str(self):
        """
        Returns the request as a XML or JSON string as it was received.

        Returns:
             String: The request as a string.
        """
        return self._request

    def _parse_request(self):
        """
        Parses the request and obtains the update tasks to perform.
        """
        try:
            request_msg = json.loads(self._request)
        except json.decoder.JSONDecodeError:
            raise ValueError(f"{self._INVALID_REQUEST_ERROR} '{self._request}'") from None
        else:
            self._parse_json_request(request_msg)

    def _parse_json_request(self, request):
        """
        Parses a JSON request and obtains the update tasks to perform.

        Args:
            request (Dictionary): The JSON request.
        """
        if not request:
            raise ValueError(f"{self._INVALID_REQUEST_ERROR} '{self._request}'")

        task_list = request.get("tasks", [])
        if not task_list:
            raise ValueError(f"{self._INVALID_REQUEST_ERROR} '{self._request}'")

        for task in task_list:
            target_obj = task.get("target", None)
            if not target_obj:
                self._show_error(f"{self._INVALID_TASK_ERROR}: no target found for task")
                continue

            type_str = target_obj.get("type", None)
            if type_str is None:  # 0 is a valid value
                self._show_error(f"{self._INVALID_TASK_ERROR}: no target type found for task")
                continue
            target_type = UpdateType.get(type_str)
            if not target_type:
                self._show_error(
                    f"{self._INVALID_TASK_ERROR}: invalid target type '{type_str}'")
                continue

            target = target_obj.get("value", None)
            if target is None:  # 0 is a valid value
                self._show_error(f"{self._INVALID_TASK_ERROR}: no target value found for task")
                continue

            profile = task.get("profile", None)
            if not profile:
                self._show_error(f"{self._INVALID_TASK_ERROR}: no profile found for task")
                continue
            if not profile.endswith(".xpro"):
                profile = f"{profile}.xpro"
            xpro_path = os.path.join(self._PROFILE_PATH, profile)
            if not os.path.isfile(xpro_path):
                self._show_error(
                    f"{self._INVALID_TASK_ERROR}: '{task.get('profile', None)}' does not exist")
                continue

            timeout = task.get("timeout", None)
            if timeout is None:
                log.info("Timeout not provided, using default")
            elif not isinstance(timeout, int) or timeout <= 0:
                log.info("Invalid timeout value (%s), using default", timeout)
                timeout = None

            self._get_update_task(target_type, target, xpro_path, timeout=timeout)

    def _get_update_task(self, target_type, target, xpro_path, timeout=None):
        """
        Builds tasks list depending on the target type.

        Args:
            target_type (:class:`.UpdateType`): Type of the task.
            target (Int or String): A role number or name, 64-bit address of a
                node, or a comma-separated list of 64-bit addresses.
            xpro_path (String): Absolute path of the '.xpro' file in the gateway.
            timeout (Integer, optional, default=`None`): Maximum time to wait
                for target read operations during the apply profile.
        """
        if target_type == UpdateType.ROLE:
            self._get_update_tasks_from_role(target, xpro_path, timeout=timeout)
        elif target_type == UpdateType.NODE:
            self._get_update_tasks_from_64bit_addr(target, xpro_path, timeout=timeout)
        elif target_type == UpdateType.GROUP:
            self._get_update_tasks_from_group(target, xpro_path, timeout=timeout)

    def _get_update_tasks_from_role(self, role, xpro_path, timeout=None):
        """
        Adds update tasks for nodes with the provided role.

        Params:
            role (Int or String): Role string: '0' (coordinator) '1' (router),
                '2' (end device).
            xpro_path (String): Absolute path of the '.xpro' file in the gateway.
            timeout (Integer, optional, default=`None`): Maximum time to wait
                for target read operations during the apply profile.

        Raises:
            ValueError: If provided role is invalid and invalid tasks are not
                ignored.
        """
        if isinstance(role, int):
            role_int = role
        try:
            role_int = int(role)
        except ValueError:
            self._show_error(
                f"{self._INVALID_TASK_ERROR}: invalid role '{role}'. Use 0, 1, or 2")
            return

        role_val = Role.get(role_int)
        if not role_val or role_val == Role.UNKNOWN:
            self._show_error(
                f"{self._INVALID_TASK_ERROR}: invalid role '{role}'. Use 0, 1, or 2")
            return

        self._update_tasks.update({role_val: (xpro_path, timeout)})

    def _get_update_tasks_from_64bit_addr(self, x64bit_str, xpro_path, timeout=None):
        """
        Adds update tasks for node with the provided 64-bit address.

        Params:
            x64bit_str (String): 64-bit address of the node.
            xpro_path (String): Absolute path of the '.xpro' file in the gateway.
            timeout (Integer, optional, default=`None`): Maximum time to wait
                for target read operations during the apply profile.
        """
        if not XBee64BitAddress.is_valid(x64bit_str):
            log.warning("%s: invalid 64-bit address '%s'",
                        self._INVALID_TASK_ERROR, x64bit_str)
            return

        self._update_tasks.update(
            {XBee64BitAddress.from_hex_string(x64bit_str): (xpro_path, timeout)})

    def _get_update_tasks_from_group(self, group_addrs, xpro_path, timeout=None):
        """
        Adds update tasks for nodes with the provided 64-bit addresses.

        Params:
            group_addrs (String): String with the 64-bit address of the nodes
                separated by commas.
            xpro_path (String): Absolute path of the '.xpro' file in the gateway.
            timeout (Integer, optional, default=`None`): Maximum time to wait
                for target read operations during the apply profile.
        """
        if group_addrs.endswith(self._GROUP_SEPARATOR):
            group_addrs = group_addrs[:-1]
        x64_list = group_addrs.split(self._GROUP_SEPARATOR)
        for x64_addr in x64_list:
            self._get_update_tasks_from_64bit_addr(x64_addr, xpro_path, timeout)

    def _show_error(self, msg):
        """
        Logs a warning with the provided message if invalid tasks must be
        ignored, raises a ValueError otherwise.

        Params:
            msg (String): Warning or exception message.

        Raises:
             ValueError: If invalid tasks are not ignored.
        """
        if not self._ignore_invalid_tasks:
            raise ValueError(msg)
        log.warning(msg)


class NetworkUpdater(Thread):
    """
    Class to perform XBee update tasks.
    """

    _XBEE_NET_UPDATE_TARGET = "xbee_network_update"

    def __init__(self, discover_network=False, ignore_invalid_tasks=False):
        """
        Class constructor. Instantiates a new :class:`.NetworkUpdater`.

        Args:
            discover_network (Boolean, optional, default=`False`): `True` to
                perform a network discovery before starting an update. `False`
                otherwise.
            ignore_invalid_tasks (Boolean, optional, default=`False`): `True`
                to process update requests with invalid tasks, `False` otherwise.

        Raises:
            XBeeException: if the local XBee is not ready.
        """
        super().__init__(daemon=True)
        self._discover_network = discover_network
        self._ignore_invalid_tasks = ignore_invalid_tasks
        self._local_xb = xbee.get_device()
        self._request = None
        self._new_request_event = Event()
        self._stop = False
        self._xbee_status = None

    def connect(self):
        """
        Opens the connection with the local XBee.

        Raises:
            XBeeException: If cannot connect with the local XBee.
        """
        self._local_xb.open()

        xbee.add_status_changed_callback(self._xbee_status_cb)

        log.debug("Registering device request for target '%s'",
                  self._XBEE_NET_UPDATE_TARGET)
        device_request.register(self._XBEE_NET_UPDATE_TARGET,
                                self._drm_request_cb,
                                status_callback=self._drm_receive_status_cb,
                                xml_encoding="UTF-8")

        self._local_xb.get_network().add_update_progress_callback(
            self._update_progress_cb)

    def run(self):
        xnet = self._local_xb.get_network()

        while not self._stop and self._local_xb.is_open():
            self._new_request_event.clear()
            while not self._new_request_event.wait(timeout=1):
                continue

            if self._discover_network:
                log.info("Discovering XBee network")
                if not xnet.is_discovery_running():
                    xnet.start_discovery_process(deep=True)
                while xnet.is_discovery_running():
                    time.sleep(0.5)

            update_tasks = self._get_update_tasks()
            self._process_update_request(update_tasks)

        if self._local_xb.is_open():
            xnet.del_update_progress_callback(self._update_progress_cb)
            self._local_xb.close()

        xbee.del_status_changed_callback(self._xbee_status_cb)

        if not device_request.unregister(self._XBEE_NET_UPDATE_TARGET):
            log.error("Unable to unregister device request for target '%s'",
                      self._XBEE_NET_UPDATE_TARGET)

    def stop(self):
        """
        Stops the network updater if it is running.
        """
        self._stop = True

    def is_ready(self):
        """
        Returns whether this instance is ready to process requests.

        Returns:
            Tuple (Boolean, String):
                Boolean: `True` if it is ready, `False` otherwise.
                String: Status description, `None` if ready.
        """
        status = None
        if self._stop:
            status = f"{APP_NAME} not ready: network updater stopped"

        if not self._local_xb.is_open():
            status = f"{APP_NAME} not ready: XBee connection not established"

        if not self._xbee_status:
            status = f"{APP_NAME} not ready: XBee connection not established"

        # 0: code, 1: XBee available, 2: status description
        if not self._xbee_status[1]:  # XBee not available
            status = f"{APP_NAME} not ready: {self._xbee_status[2]}"

        # code: 2 = LOCAL_UPDATE_IN_PROGRESS
        # code: 3 = REMOTE_UPDATE_IN_PROGRESS
        # code: 4 = RECOVERY_IN_PROGRESS
        if self._xbee_status[0] in (2, 3, 4):
            status = f"{APP_NAME} not ready: {self._xbee_status[2]}"

        if status:
            return False, status

        return True, None

    def is_processing_request(self):
        """
        Returns whether this instance is processing an update request.

        Returns:
            Boolean: `True` if a request is in progress, `False` otherwise.
        """
        return self._new_request_event.is_set()

    def _drm_request_cb(self, target, request):
        """
        Callback to handle device requests from Digi Remote Manager.

        Params:
            target (String): Device request target.
            request (String): Contents of device request.

        Returns:
            String: Or str-convertible object as response of the device request.
        """
        log.debug("Received device request for target '%s': %s", target, request)

        ready, desc = self.is_ready()
        if not ready:
            ret = f"Ignoring update task request: {desc}"
            log.warning(ret)
            return ret

        try:
            update_request = UpdateRequest(
                request, ignore_invalid_tasks=self._ignore_invalid_tasks)
        except ValueError as exc:
            log.error(exc)
            return exc

        self._set_request(update_request)

        return ""

    def _drm_receive_status_cb(self, error, desc):
        """
        Callback function called the receive process is complete. It provides
        overall error status.

        Args:
            error (Integer): 0 for success, and other positive values for
                different errors.
            desc (String): Indication of the problem. "Success" for error code 0.
        """
        log.debug("Received status for request target '%s': %s (%d)",
                  self._XBEE_NET_UPDATE_TARGET, desc, error)

    @staticmethod
    def _update_progress_cb(node, progress_status):
        log.debug("%s - [%s] %s: %d%%", progress_status.type, node,
                  progress_status.task, progress_status.percent)
        if progress_status.finished:
            log.info("'%s' updated: %s", node, progress_status.task)

    def _xbee_status_cb(self, code, desc, available):
        """
        Callback to notify changes of the status of the XBee connection.

        Args:
            code (Integer): Integer indicating the current status.
            desc (String): String indicating the status ("Online", "Offline",
                "Local update process in progress", ...). It matches the
                `code` value.
            available (Boolean): `True` if the XBee is available for operations,
                `False` otherwise. When it is not available, any operation with
                the XBee will timeout.
        """
        # code: 0 = ONLINE
        # code: 1 = OFFLINE
        # code: 2 = LOCAL_UPDATE_IN_PROGRESS
        # code: 3 = REMOTE_UPDATE_IN_PROGRESS
        # code: 4 = RECOVERY_IN_PROGRESS
        # code: 5 = NET_DISCOVERY_IN_PROGRESS
        # code: 6 = NEIGHBOR_DISCOVERY_IN_PROGRESS
        # code: 7 = NETWORK_FIND_IN_PROGRESS
        # code: 8 = ACTIVE_DISCOVERY_IN_PROGRESS
        self._xbee_status = (code, available, desc)
        if code == 1:
            stop_event.set()

    def _process_update_request(self, update_tasks):
        """
        Performs the update tasks in the request being processed.

        Params:
            update_tasks (Dict): Dictionary with the 64-bit address as key and
                the corresponding :class::`.ProfileUpdateTask` as value.
        """
        if not update_tasks:
            log.error("No update tasks to perform")
            return

        if log.isEnabledFor(logging.INFO):
            log.info("Request received to update the following XBee targets:")
            for task in update_tasks.values():
                log.info("  * '%s' to '%s'", task.xbee, task.profile_path)

        xnet = self._local_xb.get_network()
        result = xnet.update_nodes(update_tasks.values())
        if log.isEnabledFor(logging.INFO):
            self._show_result(result, update_tasks)

        # Clear the update tasks after finishing
        update_tasks.clear()
        self._request = None

    def _set_request(self, request):
        """
        Establishes the received request to be processed.

        Params:
            request (:class::`.UpdateRequest`): The update request.
        """
        if not self._request and not self.is_processing_request():
            self._request = request
            self._new_request_event.set()
        else:
            log.warning("Ignoring update task request, there is an update in progress")

    def _get_update_tasks(self):
        """
        Parses the request and obtains the update tasks to perform.

        Returns:
            Dict: Dictionary with the 64-bit address as key and the
                corresponding :class::`.ProfileUpdateTask` as value.
        """
        update_tasks = {}
        for req_task in self._request.tasks.items():
            tasks = None
            if isinstance(req_task[0], XBee64BitAddress):
                tasks = [self._get_tasks_from_64bit_addr(req_task[0], *req_task[1])]
            elif isinstance(req_task[0], Role):
                tasks = self._get_tasks_from_role(req_task[0], *req_task[1])
            self._add_tasks(tasks, update_tasks)

        return update_tasks

    def _get_tasks_from_role(self, role, profile, timeout=None):
        """
        Creates the update tasks for nodes with the provided role.

        Params:
            role (:class::`.Role`): Role of nodes to update.
            profile (String): Absolute path of the '.xpro' file in the gateway.
            timeout (Integer, optional, default=`None`): Maximum time to wait
                for target read operations during the apply profile.

        Returns:
            List: List of created :class::`.ProfileUpdateTask`.
        """
        xnet = self._local_xb.get_network()
        node_list = xnet.get_devices()
        node_list.append(self._local_xb)
        role_tasks = []
        for node in node_list:
            node_role = node.get_role()
            if node_role and node_role != role:
                continue
            role_tasks.append(ProfileUpdateTask(node, profile, timeout=timeout))

        return role_tasks

    def _get_tasks_from_64bit_addr(self, x64_addr, profile, timeout=None):
        """
        Creates the update task for node with the provided 64-bit address.

        Params:
            x64_addr (:class::`.XBee64BitAddress`): 64-bit address of the node.
            profile (String): Absolute path of the '.xpro' file in the gateway.
            timeout (Integer, optional, default=`None`): Maximum time to wait
                for target read operations during the apply profile.

        Returns:
            :class::`.ProfileUpdateTask`: The update task.
        """
        if self._local_xb.get_64bit_addr() == x64_addr:
            node = self._local_xb
        else:
            xnet = self._local_xb.get_network()
            node = xnet.get_device_by_64(x64_addr)

        if not node:
            log.info("Node with 64-bit address '%s' not in discovered network", x64_addr)
            node = RemoteXBeeDevice(local_xbee=self._local_xb, x64bit_addr=x64_addr)

        return ProfileUpdateTask(node, profile, timeout=timeout)

    @staticmethod
    def _add_tasks(tasks, update_tasks):
        """
        Adds the provided update tasks to the list. If there is another task
        for the same node in the list, nothing is added and a warning is logged.

        Params:
            task (List): List of :class::`.ProfileUpdateTask`to add.
            update_tasks (Dictionary): Dictionary to add the task.
        """
        if not tasks:
            return
        for task in tasks:
            node_addr = str(task.xbee.get_64bit_addr())
            if node_addr not in update_tasks:
                update_tasks.update({node_addr: task})
            else:
                log.warning("Task for node %s already provided", task.xbee)

    @staticmethod
    def _show_result(result, update_tasks):
        """
        Logs the result after performing all update tasks in the request.

        Params:
            result (Dict): Uses the 64-bit address of the XBee as key and, as
                value, a Tuple with the XBee (:class:`.AbstractXBeeDevice`) and
                an :class:`.XBeeException` if the process failed for that node
                (`None` if it successes)
            update_tasks (Dict): Dictionary with the 64-bit address as key and
                the corresponding :class::`.ProfileUpdateTask` as value.
        """
        msg = [["Node", "Profile path", "Result"]]
        row_len = [len(msg[0][0]), len(msg[0][1]), len(msg[0][2])]
        for task in update_tasks.values():
            res = result.get(str(task.xbee.get_64bit_addr()), None)
            if res and res[1]:
                res_msg = f"ERROR: {str(res[1])}"
            else:
                res_msg = "OK"
            row_len = [max(len(str(task.xbee)), row_len[0]),
                       max(len(task.profile_path), row_len[1]),
                       max(len(res_msg), row_len[2])]
            msg.append([str(task.xbee), task.profile_path, res_msg])

        log.info("\nSummary:\n")
        row_format = "  ".join(["{: <%d}"] * len(row_len)) % tuple(row_len)
        for row in msg:
            log.info(row_format.format(*row))
            log.info("")


def init_log(log_level, log_console):
    """
    Initialize console and syslog loggers.

    Args:
        log_level (String): The file logger level.
        log_console (Boolean): `True` to log to console, `False` otherwise.
    """
    log_format = "%(name)s: %(message)s"
    level = logging.INFO
    handlers = []

    if log_level == "D":
        level = logging.DEBUG
    elif log_level == "I":
        level = logging.INFO
    elif log_level == "W":
        level = logging.WARNING
    elif log_level == "E":
        level = logging.ERROR

    def configure_handler(log_handler, name, fmt, handlers_list):
        log_handler.name = name
        log_handler.setFormatter(
            logging.Formatter(fmt=fmt, datefmt='%Y-%m-%d,%H:%M:%S'))
        log_handler.setLevel(level)
        handlers_list.append(log_handler)

    if log_console:
        log_console_format = "%(asctime)s %(name)s: %(message)s"
        configure_handler(logging.StreamHandler(), "%s console handler",
                          log_console_format, handlers)
    configure_handler(SysLogHandler(address='/dev/log'), "%s syslog handler",
                      log_format, handlers)

    loggers = [log]
    for logger in loggers:
        logger.disabled = False
        logger.setLevel(level)
        for handler in handlers:
            logger.addHandler(handler)


def signal_handler(signal_number, _frame):
    """
    Signal handler function.

    Args:
        signal_number (Integer): Received signal.
        _frame: Current stack frame.
    """
    if signal_number in (signal.SIGTERM, signal.SIGINT, signal.SIGQUIT):
        stop_event.set()


def main():
    """
    Main execution method.
    """
    parser = argparse.ArgumentParser(description='Update XBee modules from Digi Remote Manager',
                                     add_help=True,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--discover", action="store_true", dest="discover",
                        help="Discover network before performing an update")
    parser.add_argument("-i", "--ignore-invalid-tasks", action='store_true',
                        dest="ignore_invalid_tasks",
                        help="Ignore invalid tasks in received requests")
    parser.add_argument("--log-console", action='store_true',
                        dest="log_console",
                        help="Enable log to standard output")
    parser.add_argument("--log-level", metavar="<D, I, W, E>", default='I',
                        choices=['D', 'I', 'W', 'E'],
                        help="Log level: debug, info, warning, error")

    args = parser.parse_args()

    init_log(args.log_level, args.log_console)

    log.info("+--------------------------+")
    log.info("| %s |", APP_NAME)
    log.info("+--------------------------+\n")

    # Register callbacks for signals processing.
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGQUIT, signal_handler)

    log.info("Configuration:")
    log.info(" * Discover XBee network:  %s", "Enabled" if args.discover else "Disabled")
    log.info(" * Ignore invalid tasks:   %s", "Yes" if args.ignore_invalid_tasks else "No")
    log.info(" * Log level:              %s", logging.getLevelName(log.getEffectiveLevel()))
    log.info(" * Log to console:         %s\n", "Enabled" if args.log_console else "Disabled")

    try:
        updater = NetworkUpdater(discover_network=args.discover,
                                 ignore_invalid_tasks=args.ignore_invalid_tasks)
        updater.connect()
    except XBeeException as exc:
        log.error("Unable to establish connection with local XBee: %s", exc)
        sys.exit(1)

    updater.start()

    log.info("Waiting for incoming XBee network update requests...\n")
    stop_event.wait()

    updater.stop()
    log.info("%s stopped", APP_NAME)


if __name__ == '__main__':
    main()
