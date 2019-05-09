#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model import singleton_test

s = singleton_test()
print(id(s))
s1 = singleton_test()
print(id(s1))
