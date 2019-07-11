#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想在类被定义的时候就初始化一部分类的成员，而不是要等到实例被创建后。

# 在类定义时就执行初始化或设置操作是元类的一个典型应用场景。本质上讲，一个元类会在定义时被触发， 这时候你可以执行一些额外的操作。

import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls, args)


# 这段代码可以用来定义简单的基于元组的数据结构，如下所示：
class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fields = ['x', 'y']


s = Stock('ACME', 50, 91.1)
print(s)  # ('ACME', 50, 91.1)
print(s[0])  # ACME
print(s.name)  # ACME
print(s.shares * s.price)  # 4555.0
s.shares = 23  # AttributeError: can't set attribute
