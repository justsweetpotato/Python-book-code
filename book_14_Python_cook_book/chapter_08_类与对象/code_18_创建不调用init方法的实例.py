#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)
print(d)

data = {'year': 2012, 'month': 12, 'day': 21}
for key, value in data.items():
    setattr(d, key, value)

print(d.year)

# ------- 我是分割线 --------

from time import localtime


class Date2:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


print(Date2.today().year)
