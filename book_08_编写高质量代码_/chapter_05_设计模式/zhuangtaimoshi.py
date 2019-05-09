#!/usr/bin/env python
# -*- coding: utf-8 -*-

def workday():
    print("工作日!")


def weekend():
    print("假日!")


class People(object):
    pass


p = People()

# while True:
for i in range(1, 8):
    if i == 6:
        p.day = weekend
    if i == 1:
        p.day = workday
    p.day()
