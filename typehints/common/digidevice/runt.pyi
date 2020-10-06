"""
APIs for accessing and modifying the device runtime database.

This module allows you to interface with the DAL runtime database (runtd):

    from digidevice import runt

    # Open the runtime database.
    runt.start()

    # Display available keys in the runtime database.
    print(runt.keys(""))

    # Make changes to the runtime database.
    runt.set("my-variable", "my-value")

    # Close the runtime database.
    runt.close()

Check help(runt) for more details.
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

from types import TracebackType
from typing import Any, List, Optional, Type, TypeVar

def start() -> None:
    """
    Starts the connection to runtd. Must be called before any methods may
    communicate with runtd.

    :raises: RuntException if the operation fails.
    """
    ...

def stop() -> None:
    """
    Stops the connection to runtd.
    """
    ...

def get(path: str) -> Any:
    """
    Gets a value stored in runt.

    :param path: The path of the value in runt

    :return: The string stored in runt, or None if the path is not populated.

    :raises: RuntException if the operation fails.
    """
    ...

def set(path: str, value: str) -> None:
    """
    Sets a value in runt.

    :param path: The path of the value in runt
    :param value: The value to set into runt. Only str values are allowed.

    :raises: RuntException when setting the value fails.
    :raises: ValueError when any argument is not a str.
    """
    ...

def delete(path: str) -> None:
    """
    Deletes a value from runt.

    :param path: The path of the value in runt.

    :raises: RuntException when the operation fails.
    """
    ...

def keys(path: str) -> List:
    """
    Gets a list of keys in the specified path in runt.

    :param path: The path in runt.

    :return: The list of keys under the path.
    """
    ...

def edit_start() -> None:
    """
    Starts an edit context. set(path, value) calls will be batched together
    and sent to runtd in one ubus message when edit_commit() is called.

    :raises: RuntException when the operation fails.
    """
    ...

def edit_commit() -> None:
    """
    Sends the contents of the edit context to runtd and clear the context.

    :raises: RuntException when the operation fails.
    """
    ...

def edit_clear() -> None:
    """
    Clears the edit context.

    :raises: RuntException when the operation fails.
    """
    ...

def edit() -> Edit:
    """
    Returns an object that can be used with Python's 'with' statement to
    manage an edit context.

    :Example:

        from acl import runt
        runt.start()
        with runt.edit():
            runt.set('a.b', 3)
            runt.set('a.c', 4)
        runt.stop()

    :return: An object edit context for use with 'with' statement.
    """
    ...


class Edit:
    T = TypeVar('T')

    def __enter__(self) -> T:
        ...

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> Optional[bool]:
        ...
