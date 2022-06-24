"""
APIs for accessing the application monitor daemon.

This module allows to access and interact with the application monitor daemon:

    from digidevice import appmonitor
    from digidevice.appmonitor import AppMonitorAction

    mon_handle = AppMonitor.register_app(5000, AppMonitorAction.RESTART,
                                         "<restart_command_to_execute>")
    mon_handle.refresh()
    . . .
    mon_handle.unregister()
"""
# Copyright 2022, Digi International Inc.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from enum import Enum


class AppMonitorError(Exception):
    """
    Exception raised when an error occurs in the application monitor daemon.
    """


class AppMonitorAction(Enum):
    """
    Enum for the available application monitor actions.
    """
    KILL = ...
    RESTART = ...
    REBOOT = ...

    def __str__(self):
        """
        The string representation of this ``AppMonitorAction``.
        """
        ...

    def __int__(self):
        """
        Class constructor. Instantiates a ``AppMonitorAction`` object.
        """
        ...


class _AppMonitorHandler:
    """
    Helper class used to interact with the Application Monitor daemon after an application
    is registered.
    """

    def __init__(self, app_id: int, timeout: int, action: AppMonitorAction, restart_command: str = ""):
        """
        Class constructor. Instantiates a new :class:`AppMonitorHandler` with the given parameters.

        :param app_id: Application ID obtained from the registration call.
        :param timeout: The configured application timeout.
        :param action: The configured application action as :class:`AppMonitorAction`
        :param restart_command: The configured application restart command.
        """
        ...

    @property
    def timeout(self) -> int:
        """
        Returns the timeout configured for the application.

        :return: The configured application timeout.
        """
        ...

    @property
    def action(self) -> AppMonitorAction:
        """
        Returns the action configured for the application.

        :return: :class:`AppMonitorAction` The configured application action.
        """
        ...

    @property
    def restart_command(self) -> str:
        """
        Returns the command to execute after the application is killed.

        Only takes effect when the configured application action is AppMonitorAction.RESTART

        :return: The configured application restart command.
        """
        ...

    def refresh(self) -> None:
        """
        Refreshes the application in the application monitor daemon.

        If the monitor daemon is not refreshed by the application in the configured timeout
        because the registered application hangs or ends unexpectedly, the daemon will execute
        the action configured in the registration process.

        The application can be unregistered from the application monitor daemon at any time by
        calling the unregister function.

        Usage::
            mon_handle.refresh()

        :raises AppMonitorError if there is any error refreshing the application.
        """
        ...

    def unregister(self) -> None:
        """
        Unregisters the application from the application monitor daemon.

        Usage::
            mon_handle.unregister()

        :raises AppMonitorError if there is any error unregistering the application.
        """
        ...


def register_app(timeout: int, action: AppMonitorAction, restart_command: str = None) -> _AppMonitorHandler:
    """
    Registers a new application to the application monitor daemon with the given data.

    If the register process succeeds, an :class:`AppMonitorHandler` is returned to use in further
    communications with the application monitor daemon.

    The application should now start sending refresh requests to the application monitor
    daemon with an interval lower than the configured timeout.

    If the monitor daemon is not refreshed by the application in the configured timeout
    because the registered application hangs or ends unexpectedly, the daemon will execute
    the action configured in the registration process.

    The application can be unregistered from the application monitor daemon at any time by
    calling the unregister function.

    Available register actions are:
        AppMonitorAction.KILL: Kill the application
        AppMonitorAction.RESTART: Kill the application and execute the provided restart command
        AppMonitorAction.REBOOT: Reboot the device

    Usage::
        from digidevice import appmonitor
        from digidevice.appmonitor import AppMonitorAction

        mon_handle = appmonitor.register_app(5000, AppMonitorAction.KILL)
        mon_handle = appmonitor.register_app(5000, AppMonitorAction.REBOOT)
        mon_handle = appmonitor.register_app(5000, AppMonitorAction.RESTART, "<restart_command>")

    :param timeout: Maximum amount of time -in milliseconds- to wait without a refresh to
                    consider the application dead or hang.
    :param action: :class:`AppMonitorAction` Action to execute when the application dies
                   or hangs.
    :param restart_command: Command to execute after application is killed when the configured action
                            is RESTART.

    :raises ValueError if pid, timeout, or action is not valid.
    :raises AppMonitorError if there is any error registering the application

    :return: :class:`AppMonitorHandler` handler to use to refresh or unregister the application from
             the Application Monitor daemon .
    """
    ...
