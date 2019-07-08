#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想通过改变实例创建方式来实现单例、缓存或其他类似的特性。

# 如果你想自定义这个步骤，你可以定义一个元类并自己实现 __call__() 方法。

# 为了演示，假设你不想任何人创建这个类的实例：

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantuate directly")


class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')


Spam.grok(42)
s = Spam()

