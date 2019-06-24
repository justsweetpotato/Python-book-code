#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq

a = [1, 3, 5, 7, 9]
b = [0, 2, 4, 6, 8]

for c in heapq.merge(a, b):
    print(c)
