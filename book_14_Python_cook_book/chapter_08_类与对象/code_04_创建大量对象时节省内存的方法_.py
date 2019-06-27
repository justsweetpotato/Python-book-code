#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date(1984, 1, 1)
print(d.year, d.month, d.day)
# print(d.__dict__)
d.year = 2019
print(d.year, d.month, d.day)
