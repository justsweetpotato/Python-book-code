#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PropertyTest(object):
    def __init__(self):
        self.var1 = 20

    @property
    def x(self):
        return self.var1


pt = PropertyTest()
print(pt.x)
pt.x = 12
