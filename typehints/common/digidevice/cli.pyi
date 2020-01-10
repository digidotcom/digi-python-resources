"""
APIs for running device CLI commands.

This module enables the execution of device CLI commands:

    from digidevice import cli

    version = cli.execute("show version")

Check help(cli.execute) for more details and parameters.
"""
# Copyright 2020, Digi International Inc.
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


class CommandFailedException(RuntimeError):
    """
    Exception generated when a command ends in error. Its message contains any
    captured output from the command before any error was detected.
    """

    def __init__(self, output: str = "") -> None:
        """
        Class constructor. Instantiates a new ``CommandFailedException`` object
        with the provided parameters.

        :param output: Any captured output from the command before any error
            was detected.
        """
        ...

    def __str__(self) -> str:
        """
        String representation of this ``CommandFailedException``.
        """
        ...


def execute(command: str, timeout: int = 5) -> None:
    """
    Executes a CLI command with the timeout specified returning the results.

    Usage::

        resp = cli.execute("show version", timeout=5)

    :param command: the full command to execute.
    :param timeout: the timeout in seconds (the default is 5 seconds).

    :return: The output produced by the command.

    :raises CommandFailedException if a command failure is detected.
    :raises TimeoutError if the timeout elapses before the command finishes.
    """
    ...