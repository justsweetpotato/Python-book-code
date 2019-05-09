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


if __name__ == '__main__':
    print(get_FileCreateTime('./1.txt'))
    print(get_FileCreateTime('./3.txt'))
    print(get_FileModifyTime('./1.txt'))
    print(get_FileModifyTime('./3.txt'))
    print(get_FileAccessTime('./1.txt'))
    print(get_FileSize('./1.txt'))