#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']

for i in zip(a, b):
    print(i)

print('-' * 50)
from itertools import zip_longest

for i in zip_longest(a, b):
    print(i)

print('-' * 50)
for i in zip_longest(a, b, fillvalue=0):
    print(i)

print('-' * 50)
from itertools import chain

x = [1, 2, 3, 4]
y = ['x', 'y', 'z']

for x in chain(x, y):
    print(x, end='')
