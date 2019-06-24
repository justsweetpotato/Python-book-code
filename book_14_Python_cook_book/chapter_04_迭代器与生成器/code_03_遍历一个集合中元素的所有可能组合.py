#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations

items = ['a', 'b', 'c']

for p in permutations(items):
    print(p)

for p in permutations(items, 2):
    print(p)

print('-' * 50)
# 不重复的排列组合
from itertools import combinations

for c in combinations(items, 3):
    print(c)

for c in combinations(items, 2):
    print(c)
