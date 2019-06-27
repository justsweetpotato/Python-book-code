#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# 抽象类的一个特点是它不能直接被实例化，抽象类的目的就是让别的类继承它并实现特定的抽象方法

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


# 除了继承这种方式外，还可以通过注册方式来让某个类实现抽象基类

import io

IStream.register(io.IOBase)
try:
    f = open('foo.txt')
except:
    with open('foo.txt', 'w') as f:
        f.write('Hello')

print(isinstance(f, IStream))
