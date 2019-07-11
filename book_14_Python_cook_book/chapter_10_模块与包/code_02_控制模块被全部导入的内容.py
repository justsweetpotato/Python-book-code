#!/usr/bin/env python
# -*- coding: utf-8 -*-

# somemodule.py
def spam():
    pass

def grok():
    pass

blah = 42
# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']


# 当从其他文件 使用 from somemodule import * 将只有 __all__ 中的被导入