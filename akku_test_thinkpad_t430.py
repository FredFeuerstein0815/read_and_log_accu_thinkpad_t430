#!/usr/bin/env python3

import datetime
from os import system
from time import sleep

DATEI = "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A08:00/device:08/PNP0C09:00/PNP0C0A:00/power_supply/BAT0/hwmon1/in0_input"
log = "akkuzellen_laufzeit_test.log"

def main():
    startzeit = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(startzeit)
    with open(log, "w") as l:
        l.write(str("\nBeginn der Messung: {}".format(startzeit)))
    while True:
        with open(DATEI, "r") as spannungsdatei:
            v = int(spannungsdatei.read())
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cls = lambda: system('clear')
            cls()
            gesamt = v/1000
            print("{0:.2f} Volt insgesamt".format(gesamt))
            zelle = gesamt/3
            print("{0:.2f} Volt pro Zelle".format(zelle))
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(log, "a") as l:
                l.write(str("\n{0}\n {1:.2f} Volt gesamt\n {2:.2f} pro Zelle\n".format(now, gesamt, zelle)))
            sleep(60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Abbruch")

