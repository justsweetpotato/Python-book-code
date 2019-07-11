#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 通常情况下，如果要写一个上下文管理器，你需要定义一个类，里面包含一个 __enter__() 和一个 __exit__() 方法，如下所示：

import time


class timethis:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))


with timethis('耗时') as t:
    n = 10000000
    while n > 0:
        n -= 1
# 耗时: 1.266099452972412

# @contextmanager 应该仅仅用来写自包含的上下文管理函数。 如果你有一些对象(比如一个文件、网络连接或锁)，需要支持 with 语句，那么你就需要单独实现 __enter__() 方法和 __exit__() 方法。
