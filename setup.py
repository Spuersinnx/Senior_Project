#!/usr/bin/env python
import pip


def install(package):
    pip.main(['install', package])


if __name__ == '__main__':
    install('pexpect')
    install ('netifaces')

