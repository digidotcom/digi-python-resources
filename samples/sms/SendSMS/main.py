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

from digidevice.sms import send

DEST = ""
MESSAGE = "Hello from the Digi device!"


def main():
    print(" +-----------------+")
    print(" | Send SMS Sample |")
    print(" +-----------------+\n")

    # Send the SMS message.
    print("- Sending SMS to '%s' >> '%s'..." % (DEST, MESSAGE))
    status, message = send(DEST, MESSAGE)
    if status:
        print("- SMS sent successfully!")
    else:
        print("- Error sending SMS >> '%s'" % message)


if __name__ == "__main__":
    main()
