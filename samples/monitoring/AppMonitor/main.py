# Copyright 2022, Digi International Inc.
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

from digidevice import appmonitor
from digidevice.appmonitor import AppMonitorAction, AppMonitorError

import sys
import time

APP_TIMEOUT = 5000


def main():
    print(" +----------------------------+")
    print(" | Application Monitor Sample |")
    print(" +----------------------------+\n")

    try:
        print("Registering application...")
        mon_handle = appmonitor.register_app(APP_TIMEOUT, AppMonitorAction.KILL)
        print("Registration succeed:\n  - Timeout: %s\n  - Action: %s\n  "
              "- Restart command: '%s'\n" % (mon_handle.timeout, mon_handle.action.name,
                                             mon_handle.restart_command))
        for loop in range(1, 6):
            print("Refreshing application... %s" % loop)
            mon_handle.refresh()
            time.sleep(0.5 * APP_TIMEOUT / 1000)
        print("\nStopped refreshing! Application should be killed in a while...")
        time.sleep(sys.maxsize)
    except AppMonitorError as exc:
        print(str(exc))
        sys.exit(1)


if __name__ == '__main__':
    main()
