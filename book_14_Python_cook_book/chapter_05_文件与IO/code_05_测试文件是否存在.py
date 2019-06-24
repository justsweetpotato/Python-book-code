#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print(os.path.exists('/etc/passwd'))

print(os.path.isfile('/etc/passwd'))

print(os.path.isdir('/etc/passwd'))

print(os.path.islink('/usr/local/bin/python3'))

print(os.path.realpath('/usr/local/bin/python3'))