#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '*.TXT'))
print(fnmatchcase('foo.txt', '*.TXT'))

