#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你在写一段代码，最终需要创建一个新的类对象。你考虑将类的定义源代码以字符串的形式发布出去。 并且使用函数比如 exec() 来执行它，但是你想寻找一个更加优雅的解决方案。

# 你可以使用函数 types.new_class() 来初始化新的类对象。 你需要做的只是提供类的名字、父类元组、关键字参数，以及一个用成员变量填充类字典的回调函数。例如：

def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost
}

import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__

s = Stock('ACME', 50, 91.1)
print(s)  # <__main__.Stock object at 0x000001913E829CF8>
print(s.cost())  # 4555.0

import abc

Stock2 = types.new_class('Stock2', (), {'metaclass': abc.ABCMeta}, lambda ns: ns.update(cls_dict))
Stock2.__module__ = __name__

print(Stock2)  # <class '__main__.Stock2'>
print(type(Stock2))  # <class 'abc.ABCMeta'>
