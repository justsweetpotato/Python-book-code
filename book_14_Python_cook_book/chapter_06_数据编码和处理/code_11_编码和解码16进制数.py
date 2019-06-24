#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = b'Hello'

import binascii

h = binascii.b2a_hex(s)
print(h)

print(binascii.a2b_hex(h))

print('第二种方法')

import base64

h = base64.b16encode(s)
print(h)

print(base64.b16decode(h))
