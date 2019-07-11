#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你有一个函数或方法，它使用 * args 和 **kwargs 作为参数，这样使得它比较通用， 但有时候你想检查传递进来的参数是不是某个你想要的类型。

# 下面是一个强制函数签名更具体的例子。在代码中，我们在基类中先定义了一个非常通用的 __init__() 方法， 然后我们强制所有的子类必须提供一个特定的参数签名。

from inspect import Signature, Parameter


def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)


class Stricture:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Stricture):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Stricture):
    __signature__ = make_sig('x', 'y')


import inspect

print(inspect.signature(Stock))
s1 = Stock('ACME', 100, 490.1)
s2 = Stock(100)

# from inspect import Signature, Parameter
#
# def make_sig(*names):
#     parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
#             for name in names]
#     return Signature(parms)
#
# class StructureMeta(type):
#     def __new__(cls, clsname, bases, clsdict):
#         clsdict['__signature__'] = make_sig(*clsdict.get('_fields',[]))
#         return super().__new__(cls, clsname, bases, clsdict)
#
# class Structure(metaclass=StructureMeta):
#     _fields = []
#     def __init__(self, *args, **kwargs):
#         bound_values = self.__signature__.bind(*args, **kwargs)
#         for name, value in bound_values.arguments.items():
#             setattr(self, name, value)
#
# # Example
# class Stock(Structure):
#     _fields = ['name', 'shares', 'price']
#
# class Point(Structure):
#     _fields = ['x', 'y']