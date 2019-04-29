#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def w1(f1):
    time.sleep(5)
    print("w1")

    def inner():
        time.sleep(5)
        print("inner")
        time.sleep(5)
        res = f1()
        print(res , "inner")

    return inner


def w2(f1):
    time.sleep(5)
    print("w2")

    def inner2():
        time.sleep(5)
        print("inner2")
        time.sleep(5)
        res = f1()
        print(res , 'inner2')

    return inner2


@w1
@w2
def f1():
    time.sleep(5)
    print("f1 我将返回值")
    return "f1"


if __name__ == '__main__':
    time.sleep(5)
    print("main")
    time.sleep(5)
    f1()
