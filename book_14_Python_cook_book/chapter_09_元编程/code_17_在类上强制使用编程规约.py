#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你的程序包含一个很大的类继承体系，你希望强制执行某些编程规约（或者代码诊断）来帮助程序员保持清醒。

# 如果你想监控类的定义，通常可以通过定义一个元类。一个基本元类通常是继承自 type 并重定义它的 __new__() 方法 或者是 __init__() 方法。比如：

# 方法一
class MyMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        return super().__new__(cls, clsname, bases, clsdict)


# 方法二
class MyMeta2(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)


# 为了使用这个元类，你通常要将它放到到一个顶级父类定义中，然后其他的类继承这个顶级父类。例如：

class Root(metaclass=MyMeta):
    pass


class A(Root):
    pass


class B(Root):
    pass


# 作为一个具体的应用例子，下面定义了一个元类，它会拒绝任何有混合大小写名字作为方法的类定义（可能是想气死Java程序员^_^）：

class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A1(Root):  # Ok
    def foo_bar(self):
        pass


class B1(Root):  # TypeError
    def fooBar(self):
        pass


