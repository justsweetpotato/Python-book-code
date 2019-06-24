#!/usr/bin/env python
# -*- coding: utf-8 -*-

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


print(list(frange(0, 4, 0.5)))
