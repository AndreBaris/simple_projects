from __future__ import print_function
import sys
import psutil
import time
from pynotifier import Notification

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def main():
    if not hasattr(psutil, "sensors_battery"):
        return sys.exit("platform not supported")
    batt = psutil.sensors_battery()
    if batt is None:
        Notification(
            title="Battery Status",
            description="No battery is installed",
            duration=5,
            urgency=Notification.URGENCY_CRITICAL
        ).send()
        time.sleep(10)
        return sys.exit("no battery is installed")

    Notification(
            title="Battery Status",
            description="Charge:    %s%%" % round(batt.percent, 2),
            duration=5,
            urgency=Notification.URGENCY_CRITICAL
        ).send()
    print("charge:     %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        Notification(
            title="Battery Status",
            description="Charging   %s" if batt.percent < 100 else "fully charged",
            duration=5,
            urgency=Notification.URGENCY_CRITICAL
        ).send()
        print("status:     %s" % (
            "charging" if batt.percent < 100 else "fully charged"))
        print("plugged in: yes")
    else:
        Notification(
            title="Battery Status",
            description="Left:     %s" % secs2hours(batt.secsleft) + "/n status:    %s" % "discharging",
            duration=5,
            urgency=Notification.URGENCY_CRITICAL
        ).send()
        print("left:       %s" % secs2hours(batt.secsleft))
        print("status:     %s" % "discharging")
        print("plugged in: no")


if __name__ == '__main__':
    main()