#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# 返回目录中所有文件列表(包括文件, 目录)
names = os.listdir('.')
print(names)

# 返回目录中的文件
names = [name for name in os.listdir('.') if os.path.isfile(os.path.join('.', name))]
print(names)

# 返回特定格式文件名
txtfiles = [name for name in os.listdir('.') if name.endswith('.txt')]
print(txtfiles)

