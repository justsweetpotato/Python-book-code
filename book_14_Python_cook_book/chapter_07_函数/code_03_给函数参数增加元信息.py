#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add(x: int, y: int) -> int:
    return x + y


help(add)
print('-' * 50)
print(add.__annotations__)
