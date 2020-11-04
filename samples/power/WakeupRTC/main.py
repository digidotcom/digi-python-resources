# Copyright 2020, Digi International Inc.
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

import re
import sys
import time

from digidevice import cli, config

# TODO: Replace with the desired date and time for the alarm.
RTC_DATE_TIME = "YYYY-MM-DD HH:MM:SS"

RTC_DATE_TIME_PATTERN = "^\d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12]\d|3[01]) (0?[0-9]|1[0-9]|2[0-3]):(0?[0-9]|[1-5][0-9])(:(0?[0-9]|[1-5][0-9]))?$"

CFG_WAKEUP_RTC = "system.power.wakeup_sources.rtc"
CFG_WAKEUP_RTC_TIME = "system.power.wakeup_sources.rtc_time"
CLI_SUSPEND = "powerctrl state suspend"


def main():
    # Verify the configured RTC date/time is valid.
    pattern = re.compile(RTC_DATE_TIME_PATTERN)
    if not pattern.match(RTC_DATE_TIME):
        print("Invalid alarm value. The RTC alarm date/time must follow this "
              "format: YYYY-MM-DD HH:MM:SS")
        sys.exit(1)

    # Configure the RTC as a wake up source with the desired time
    cfg = config.load(writable=True)
    old_wake_rtc = cfg.get(CFG_WAKEUP_RTC)
    old_wake_rtc_time = cfg.get(CFG_WAKEUP_RTC_TIME)
    cfg.set(CFG_WAKEUP_RTC, True)
    cfg.set(CFG_WAKEUP_RTC_TIME, RTC_DATE_TIME)
    cfg.commit()

    # Give time to the configuration scripts to execute
    time.sleep(2)

    # Suspend the device
    print("Going to suspend...")
    print(cli.execute(CLI_SUSPEND))

    # At this point device is awake, print a message
    print("Device is awake!")

    # Restore the old wake up RTC value
    cfg = config.load(writable=True)
    cfg.set(CFG_WAKEUP_RTC, old_wake_rtc)
    cfg.set(CFG_WAKEUP_RTC_TIME, old_wake_rtc_time)
    cfg.commit()


if __name__ == '__main__':
    main()
