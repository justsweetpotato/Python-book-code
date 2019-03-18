#!/usr/bin/env python
# -*- coding: utf-8 -*-

msg = '!dlrow olleH'

translated = ''

i = len(msg) - 1
while i >= 0:
    translated += msg[i]
    i -= 1

print(translated)

# t = msg[::-1]
# print(t)
