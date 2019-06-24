#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = 'Hello World'

print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.center(20, '-'))
print('-' * 50)
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '=^20s'))
print('-' * 50)
print('{:>10s} {:>10s}'.format('Hello', 'World'))
print('-' * 50)

x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))
