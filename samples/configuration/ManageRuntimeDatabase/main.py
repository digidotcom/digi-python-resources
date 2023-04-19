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

from digidevice import runt

NEW_VAR = "my_new_var"
NEW_VAR_VALUE = "110777"


def main():
    print(" +--------------------------------+")
    print(" | Manage Runtime Database Sample |")
    print(" +--------------------------------+\n")

    # Open the runtime database.
    runt.start()

    try:
        # Display all the available runtime keys in the database.
        print("Runtime database elements:")
        for key in runt.keys(""):
            print(" - %s" % key)
        print("\n")

        # Display the system keys of the database.
        print("System (system) elements:")
        for sys_key in runt.keys("system"):
            print(" - %s" % sys_key)
        print("\n")

        # Display the system MAC address.
        print("System MAC (system.mac) value: %s\n" % runt.get("system.mac"))

        # Add a new variable to the runtime database.
        print("Generating new variable '%s'" % NEW_VAR)
        runt.set(NEW_VAR, NEW_VAR_VALUE)
        # Print the value of the new variable.
        print(" - Value read from '%s' variable: %s" % (NEW_VAR,
                                                        runt.get(NEW_VAR)))
    finally:
        # Close the runtime database.
        runt.stop()


if __name__ == "__main__":
    main()
