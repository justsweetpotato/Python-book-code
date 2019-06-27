#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


s = SubPerson('Guido')
print(s.name)
s.name = 'Larry'


class SubPerson2(Person):
    @Person.name.getter
    def name(self):
        print('[2]Getting name')
        return super().name

    @Person.name.setter
    def name(self, value):
        print('[2]Setting name to', value)
        return super(SubPerson2, SubPerson2).name.__set__(self, value)


s2 = SubPerson2('Ming')
print(s2.name)
s2.name = 'Yong'
