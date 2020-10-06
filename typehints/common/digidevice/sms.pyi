"""
APIs for accessing the Wi-Fi scanner data.

This module provides access to the Wi-Fi scanner's output log:

    import threading
    from digidevice.sms import Callback, send

    TIMEOUT = 60

    c = threading.Condition()

    def sms_test_callback(sms):
        print("- Received SMS message from '%s' >> '%s'" % (sms['from'],
                                                            sms['message']))
        c.acquire()
        c.notify()
        c.release()

    # Send SMS.
    print "- Sending SMS message..."
    status, message = send("destination", "message")
    if status:
        print("- SMS sent successfully!")
    else:
        print("- Error sending SMS >> '%s'" % message)

    # Receive SMS.
    my_callback = Callback(sms_test_callback)

    print("\n- Send an SMS message now.")
    print("- Waiting for SMS messages...")

    # Acquire the semaphore and wait until a callback occurs.
    c.acquire()
    try:
        c.wait(TIMEOUT)
    except Exception as e:
        print("- Exception occurred while waiting for SMS")
        print(e)

    c.release()

    my_callback.unregister_callback()

Check help(sms) for more details.
"""
##############################################################################
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
# Digi International Inc., 9350 Excelsior Blvd., Suite 700, Hopkins, MN 55343
##############################################################################

from typing import Callable, Tuple


class Callback():
    """
    Callback for receiving and handling incoming SMS messages.
    """

    def __init__(self, callback: Callable, metadata: bool = False) -> None:
        """
        Creates and registers callback for SMS messages. Callback will be
        triggered when any SMS is received. Any preexisting unprocessed SMS
        messages will also trigger the callback.

        :param callback: Callback function to be used.
        :param metadata: When false the callback will be given the text of
            the message as an argument. When true the callback will be given
            the the text of the message and a dictionary containing all the
            other sms data as arguments.
        """
        ...

    def unregister_callback(self) -> None:
        """
        Unregisters callback for SMS messages. Unprocessed messages will be
        stored until a new callback is registered to process them.
        """
        ...

    def register_callback(self, callback: Callable,
                          metadata: bool = False) -> None:
        """
        Registers callback for SMS messages. Callback will be triggered when
        any SMS is received. Any preexisting unprocessed SMS messages will
        also trigger the callback.

        :param callback: Callback function to be used.
        :param metadata: When false the callback will be given the text of the
            message as an argument. When true the callback will be given the
            the text of the message and a dictionary containing all the other
            sms data as arguments.
        """
        ...


def send(number: str, message: str, timeout: float = 60) -> Tuple[bool, str]:
    """
    Sends a sms message to the given number

    :param number: Phone number to send message to.
    :param message: Message to send.

    :return: Tuple containing the return code (true if message was successfully
        sent) and the output produced by the modem during message transmission.
    """
    ...