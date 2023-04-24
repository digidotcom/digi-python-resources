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

from digidevice import cli

CLI_SYSTEM_INFO = "show system"
CLI_LIST_ROOT = "ls /"

def main():
    print(" +-----------------------------+")
    print(" | Execute CLI Commands Sample |")
    print(" +-----------------------------+\n")

    # Read system information
    print("SYSTEM INFORMATION (%s)" % CLI_SYSTEM_INFO)
    print("-" * 72)
    print(cli.execute(CLI_SYSTEM_INFO))
    print("\n")

    # List the content of the root path of the device.
    print("LIST ROOT (%s)" % CLI_LIST_ROOT)
    print("-" * 72)
    print(cli.execute(CLI_LIST_ROOT))
    print("\n")


if __name__ == "__main__":
    main()
