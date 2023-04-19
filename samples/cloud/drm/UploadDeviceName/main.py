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

from digidevice import name

# TODO: Replace with the name you desire for your device
NEW_DEVICE_NAME = "MY-DEVICE"


def main():
    print(" +---------------------------+")
    print(" | Upload Device Name Sample |")
    print(" +---------------------------+\n")

    print("Uploading device name with '%s' to Digi Remote Manager" % NEW_DEVICE_NAME)
    name.upload(NEW_DEVICE_NAME)


if __name__ == "__main__":
    main()
