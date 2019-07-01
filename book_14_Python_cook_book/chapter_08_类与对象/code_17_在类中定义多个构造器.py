#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


class Date:
    '''方法一: 使用类方法'''

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)
b = Date.today()
print(a.year)
print(b.year)
