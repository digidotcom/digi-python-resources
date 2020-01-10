"""
Python interface to DAL configuration (libconfig).

This module allows to access and modify the device configuration:

    from digidevice import config

    cfg = config.load()

Check help(led.load) for more details and parameters.
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

from typing import Any, Iterator


def load(writable: str = False):
    """
    Loads the configuration and gets a handle to the root node.

    :param writable: The access mode of the configuration.

    :return: The root ConfigNode of the configuration.

    :raises Exception if the configuration load fails.
    """
    ...

class ConfigNode:
    """
    Class that helps accessing and modifying the configuration of a device.
    """

    def __init__(self, ptr, path, root: bool = False, array: bool = False,
                 writable: bool = True) -> None:
        """
        Class constructor. Instantiates a new ``ConfigNode`` object
        with the provided parameters.

        :param ptr: The handle to the root node.
        :param path: The relative path.
        :param root: Whether this is the root node or not.
        :param array: Whether this node has an array of configurations or not.
        :param writable: Whether this node is writable or not.
        """
        ...

    def __del__(self) -> None:
        """
        Deletes the configuration of the device.
        """
        ...

    def __str__(self) -> str:
        """
        Returns the string representation of this ``ConfigNode``.
        """
        ...

    def __getitem__(self, key: str) -> Any:
        """
        Looks up the node/value using the path relative to the current node.
        Paths are period separated.

        :param key: The string representation of the path relative to the
            current node.

        :return: A ConfigNode if an object or array, the Python literal of the
            corresponding type.

        :raises Exception if the given path is invalid.
        """
        ...

    def __setitem__(self, key: str, value: str) -> None:
        """
        Sets the node/value using the path relative to the current node.

        :param key: The string representation of the path relative to the
            current node.
        :param value: The node/value to set to the current node.

        :raises Exception if the given path is invalid.
        """
        ...

    def __contains__(self, key: str) -> bool:
        """
        Returns whether this object contains the given key.

        :param key: The key to check if it is part of the array of this object.

        :return: ``True`` if this object contains the given key, ``False``
            otherwise.
        """
        ...

    def __len__(self) -> int:
        """
        Gets the number of elements in the array. These elements are numbered
        [ 0, count-1 ].

        :return: The number of elements.

        :raises Exception if this node does not represent an array.
        """
        ...

    def __iter__(self) -> Iterator[str]:
        """
        The iterator with the list of keys of this node.

        :return: The iterator with the list of keys of this node.
        """
        ...

    def get(self, path: str) -> str:
        """
        Looks up the node/value using the path relative to the current node.
        Paths are period separated.

        :param path: The string representation of the path relative to the
            current node.

        :return: The value of a configuration node based on the given path.

        :raises Exception if the given path is invalid.
        """
        ...

    def set(self, path: str, value: str) -> None:
        """
        Sets the node/value using the path relative to the current node.

        :param path: The string representation of the path relative to the
            current node.
        :param value: The node/value to set to the current node.

        :raises Exception if the given path is invalid.
        """
        ...

    def count(self) -> int:
        """
        Gets the number of elements in the array. These elements are numbered
        [ 0, count-1 ].

        :return: The number of elements.

        :raises Exception if this node does not represent an array.
        """
        ...

    def keys(self) -> list[str]:
        """
        Gets a list of the keys to this node's immediate children.
        If the node is an array, the returned list will be a range on
        [ 0, count-1 ].

        :return: A list of keys.
        """
        ...

    def dump(self, hide_private: bool = False) -> str:
        """
        Returns a string containing newline separated configuration
        key/value pairs.
        This is equivalent to "config dump" on the CLI, or "config dump-public"
        if ``hide_private=True``.

        :param hide_private: Boolean to do a "config dump-public" instead of a
            "config dump".

        :return: A string of the configuration dump.

        :raises Exception if there is any error obtaining the decoded output of
            the "config dump" or "config dump-public" commands.
        """
        ...

    def changes(self) -> str:
        """
        Shows the changes that the current configuration has from the default
        configuration.
        This is equivalent to the JSON decode of the output of "config json" on
        the CLI.

        :return: A string with the changes that the current configuration has
            from the default configuration.

        :raises Exception if there is any error obtaining the decoded output of
            the "config json" command.
        """
        ...

    def commit(self) -> bool:
        """
        Saves the configuration changes to disk. This applies only to
        configurations opened with ``writable=True``.

        :return: ``True`` if the configuration was saved successfully,
            ``False`` otherwise.

        :raises Exception if ConfigNode is not root or not writable.
        """
        ...
