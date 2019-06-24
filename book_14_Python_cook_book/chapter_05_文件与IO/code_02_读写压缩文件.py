#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip

# 读取
with gzip.open('somefile.gz', 'r') as f:
    text = f.read()
# 写入
with gzip.open('somefile.gz', 'w') as f:
    f.write(text)
# 压缩
with gzip.open('somefile.gz', 'w', compresslevel=5) as f:
    f.write(text)

import bz2

with bz2.open('somefile.bz2', 'r') as f:
    text2 = f.read()
