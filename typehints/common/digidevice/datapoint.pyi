"""
APIs for uploading data points from the device to DRM.

This module enables the uploading of various data from
the device:

    from digidevice import datapoint

    datapoint.upload("mystreamid", "myvalue")

Check help(datapoint.upload) for more details and parameters.
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

from enum import Enum
from typing import Tuple, Any, Optional


class DataType(Enum):
    """
    Optionally, the DataType enumeration can be used as an indicator for the
    data type of the stream. The Python data type does not have to match this
    data type.
    For example, its perfectly reasonable to upload a string value, but mark
    it as a double if the representation matches a double type.
    The data type is serialized into the CSV message as a string, the NAME must
    be the same as the type accepted by the server.
    """
    INT = ...
    LONG = ...
    FLOAT = ...
    DOUBLE = ...
    STRING = ...
    BINARY = ...
    JSON = ...
    GEOJSON = ...

    def __str__(self) -> None:
        """
        The string representation of this ``DataType``.
        """
        ...

    def __int__(self) -> None:
        """
        Class constructor. Instantiates a ``DataType`` object.
        """
        ...


class DataPointException(RuntimeError):
    """
    Exception generated when a data point fails to upload. Its message contains
    any captured output from the command. In the case of a server produced
    error, the value comes from the server.
    """
    def __init__(self, msg: str) -> None:
        """
        Class constructor. Instantiates a new ``DataPointException`` object
        with the provided parameters.

        :param msg: The message containing any captured output from the command.
            In the case of a server produced error, the value comes from the
            server.
        """
        ...


def upload(stream_id: str, data: Any, *, description: Optional[str] = None,
           timestamp: Optional[float] = None, units: Optional[str] = None,
           geo_location: Optional[Tuple[float, float, float]] = None,
           quality: Optional[int] = None, data_type: Optional[DataType] = None,
           timeout: Optional[float] = None) -> None:
    """
    Uploads a single data point. The stream_id and data parameters are required.
    Data is always uploaded in its string form and converted appropriately by
    the server.
    Because the data point is sent to the server and communication can fail
    at any time, it's possible for this request to fail, but the data point to
    still be successfully uploaded.

    Usage::

        datapoint.upload("health/state", 100)
        datapoint.upload("drivestats/speed", 37, units="mph", geo_location=(43.9041, -92.4916, 1302))
        datapoint.upload("heartbeat", "ok", timestamp=time.time())

    :param stream_id: The name of the stream. It will automatically have the
        Device ID prepended to it by the server.
    :param data: The data point data. For most data types, converted to string
        for upload by its __str__() method. For GEOJSON, a non-string python
        object may be passed and it is converged using json.dumps().
    :param description: Optional: The description of the data point.
    :param timestamp: Optional: A datetime object or float timestamp (as
        returned by time.time()) describing the local time the data point was
        recorded (if unset, it is automatically set by the client at the time
        of send). Local system timezone information is added to the timestamp
        unless it is specified as a datetime object.
    :param units: Optional: The current units recorded in the stream associated
        with the data point. This is a free form text.
    :param geo_location: Optional: A 2 or 3 element sequence with float values
        describing the latitude, longitude and elevation associated with the
        data point.
    :param quality: Optional: An integer describing the quality associated with
        this data point.
    :param data_type: Optional: The DataType enum constant indicating what data
        type should be used for the stream associated with the data point.
    :param timeout: Optional: The timeout in seconds before the client reports
        an error.

    :raises DataPointException if there are any server or transport problems.
    :raises TimeoutError if the request times out.
    :raises TypeError if the data value is binary instead of it being a
        bytes-like object, or if the data_type parameter is not a DataType enum.
    :raises ValueError if the value of a parameter doesn't match the expected
        one.
    """
    ...