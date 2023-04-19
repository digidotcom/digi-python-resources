# Copyright 2023, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from digidevice.sms import Callback


def main():
    print(" +--------------------+")
    print(" | Receive SMS Sample |")
    print(" +--------------------+\n")

    my_callback = Callback(sms_test_callback)

    print("- Waiting for SMS messages...")
    input()

    my_callback.unregister_callback()


def sms_test_callback(sms):
    print("- Received SMS message from '%s' >> '%s'" % (sms['from'],
                                                        sms['message']))


if __name__ == "__main__":
    main()
