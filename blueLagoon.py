#!/usr/bin/env python
import subprocess
import time
import fnmatch
import os


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
    seconds = 60
    print 'Running Bluelog for ' + str(seconds) + ' seconds\n'
    bluelog = subprocess.Popen(["bluelog", "-c", "-m", "-n"])
    time.sleep(seconds)
    bluelog.terminate()


if __name__ == '__main__':
    init()
    time.sleep(3)
    scan()
