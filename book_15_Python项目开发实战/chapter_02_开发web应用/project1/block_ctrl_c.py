#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys
import time


def signal_handler(signal, frame):
    print('强制退出。。。')
    sys.exit(0)


def loop_func():
    signal.signal(signal.SIGINT, signal_handler)
    for x in range(100):
        time.sleep(2)
        print(x)


if __name__ == '__main__':
    loop_func()
