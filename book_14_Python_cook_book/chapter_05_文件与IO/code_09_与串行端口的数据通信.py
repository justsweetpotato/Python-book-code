#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial

ser = serial.Serial('/dev/tty.usbmodem641',
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)
