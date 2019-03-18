#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


def test1():
    start = time.time()
    a_list = [i for i in range(1000)]
    a_list[1] = a_list[-1]
    a_list.pop()
    print(a_list)
    print(time.time() - start)


def test2():
    start = time.time()
    a_list = [i for i in range(1000)]
    a_list.pop(1)
    print(a_list)
    print(time.time() - start)


test1()
test2()
