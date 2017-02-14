#!/usr/bin/env python
import subprocess
import time
import fnmatch
import os
import re


def init():
    configResult = subprocess.check_output(["hciconfig"])
    interface = 'hci0'
    status = 'UP'
    if interface and status in configResult:
        print "Bluetooth adapter already enabled..\n"
    else:
        print "Enabling bluetooth adapter.."
        subprocess.call(["hciconfig", interface, "up"])


def scan():
    seconds = 30
    print 'Running Bluelog for ' + str(seconds) + ' seconds\n'
    bluelog = subprocess.Popen(["bluelog", "-c", "-m", "-n"])
    time.sleep(seconds)
    bluelog.terminate()
    time.sleep(3)


def target():
    pattern = 'bluelog-*.log'
    directory = os.listdir('.')
    macAddress = re.compile("([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})")
    logs = fnmatch.filter(directory, pattern)
    macAddrArray = set()

    for log in logs:
        with open(log) as record:
            for line in record:
                matchResult = re.search(macAddress, line)
                macAddrArray.add(matchResult.group(0))

    for item in list(macAddrArray):
        print item


if __name__ == '__main__':
    init()
    time.sleep(3)
    scan()
    target()
