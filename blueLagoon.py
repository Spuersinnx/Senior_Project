#!/usr/bin/env python
import subprocess
import time


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
    subprocess.call(["bluelog", "-c","-m","-n"])





if __name__ == '__main__':
    init()
    time.sleep(3)
    scan()
