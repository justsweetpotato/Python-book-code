#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)


def get_FileAccessTime(filePath):
    t = os.path.getatime(filePath)
    return TimeStampToTime(t)


def get_FileCreateTime(filePath):
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


def get_FileModifyTime(filePath):
    t = os.path.getmtime(filePath)
    return TimeStampToTime(t)


class P(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "OK" + str(self.x) + str(self.y)


def my_coroutine():
    while True:
        received = yield
        print('Received:', received)


def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)


if __name__ == '__main__':
    it = my_coroutine()
    next(it)
    it.send("First")
    it.send("Second")
    print('*' * 50)
    it = minimize()
    next(it)
    print(it.send(10))
    print(it.send(4))
    print(it.send(20))
    print(it.send(-1))
