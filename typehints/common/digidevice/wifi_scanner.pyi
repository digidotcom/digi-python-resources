"""
APIs for accessing the Wi-Fi scanner data.

This module provides access to the Wi-Fi scanner's output log:

    from digidevice import wifi_scanner
    scanner = wifi_scanner.WifiScanner()
    scanner.data()
    .
    .
    .
    scanner.data()
    scanner.stop()

Check help(wifi_scanner.WifiScanner) for more details and parameters.
"""
# Copyright 2020 Digi International Inc., All Rights Reserved
#
# This software contains proprietary and confidential information of Digi
# International Inc.  By accepting transfer of this copy, Recipient agrees
# to retain this software in confidence, to prevent disclosure to others,
# and to make no use of this software other than that for which it was
# delivered.  This is an unpublished copyrighted work of Digi International
# Inc.  Except as permitted by federal law, 17 USC 117, copying is strictly
# prohibited.
#
# Restricted Rights Legend
#
# Use, duplication, or disclosure by the Government is subject to
# restrictions set forth in sub-paragraph (c)(1)(ii) of The Rights in
# Technical Data and Computer Software clause at DFARS 252.227-7031 or
# subparagraphs (c)(1) and (2) of the Commercial Computer Software -
# Restricted Rights at 48 CFR 52.227-19, as applicable.
#
# Digi International Inc., 9350 Excelsior Blvd, Suite 700, Hopkins, MN 55343

from typing import List

_OUTPUT_FILE = ...
_MAX_ENTRIES = ...


class WifiScannerException(Exception):
    ...


class WifiScanner:
    def __init__(self, max: int = _MAX_ENTRIES) -> None:
        """
        Starts an instance to cache the data from the Wi-Fi scanner.

        :param max: Maximum number of Wi-Fi scanner entries to cache.
        """
        ...

    def __get_update_interval(self) -> int:
        """
        Returns the configured update interval for the Wi-Fi scanner.

        :return: The configured update interval for the Wi-Fi scanner.
        """
        ...

    def __read_output_file(self) -> None:
        """
        Reads the Wi-Fi scanner output file and caches the data.
        """
        ...

    def stop(self) -> None:
        """
        Stops the Wi-Fi scanner read thread.
        """
        ...

    def data(self) -> List[str]:
        """
        Returns a list of current Wi-Fi scanner data.

        :return: A list of current Wi-Fi scanner data.
        """
        ...
