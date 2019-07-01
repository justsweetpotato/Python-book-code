#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student():
    def __getattr__(self, item):
        return item + ' is not exits.'

    @classmethod
    def __setattr__(cls, key, value):
        setattr(cls, key, value)

    @classmethod
    def __getitem__(cls, item):
        return getattr(cls, item)


    @classmethod
    def __setitem__(cls, key, value):
        return setattr(cls, key, value)


s = Student()
print(s.age)
s.age = 19
print(s.age)
print(s.__dict__)
print(s['age'])
s['age'] = 20
print(s.age)
