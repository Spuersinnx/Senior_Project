#!/usr/bin/env python
import subprocess
import netifaces


class wiFi(object):
    wireless = ''
    wmode = ''


def init():
    interfaces = netifaces.interfaces()
    print "Interfaces available: "
    print interfaces

    wInterface = 'wlan0'
    if wInterface in interfaces:
        wiFi.wireless = wInterface
        print "\nWireless Interface: " + wiFi.wireless

    subprocess.call(["airmon-ng", "check", "kill"])
    print "Starting Wireless Card in Monitor Mode..."

    iwconfig = subprocess.check_output(["iwconfig"])
    mode = 'Monitor'
    wiFi.wmode = wInterface + 'mon'
    if wiFi.wmode and mode in iwconfig:
        print "Wireless Card already in Monitor Mode"
        # print wiFi.wmode
    else:
        subprocess.call(["airmon-ng", "start", wiFi.wireless])


def collect():
    print "Commonly-used channels 1, 6, and 11 will be monitored by default"
    monitorChannels = input('Please select any other channels you wish to monitor: ')
    subprocess.call(["airodump-ng", "-c", "1,2,3,4,5,6,7,8,9,10,11", wiFi.wireless])


if __name__ == '__main__':
    init()
