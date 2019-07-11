#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想自己去实现一个新的上下文管理器，以便使用with语句。

# 实现一个新的上下文管理器的最简单的方法就是使用 contexlib 模块中的 @contextmanager 装饰器。 下面是一个实现了代码块计时功能的上下文管理器例子：

import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1


# counting: 1.2312605381011963

# 在函数 timethis() 中，yield 之前的代码会在上下文管理器中作为 __enter__() 方法执行， 所有在 yield 之后的代码会作为 __exit__() 方法执行。 如果出现了异常，异常会在yield语句那里抛出。

# 下面是一个更加高级一点的上下文管理器，实现了列表对象上的某种事务：

@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


items = [1, 2, 3]
with list_transaction(items) as working:
    working.append(4)
    working.append(5)

print(items)  # [1, 2, 3, 4, 5]

with list_transaction(items) as working:
    working.append(6)
    working.append(7)
    raise RuntimeError('oops')

# items
# [1, 2, 3, 4, 5]
