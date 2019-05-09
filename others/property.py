#!/usr/bin/env python
# -*- coding: utf-8 -*-

class People(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        assert isinstance(age, int), "Value Error"
        self.__age = age

    @age.deleter
    def age(self):
        print("delete age")
        del self.__age


obj = People("Jack", 19)
print("Jack's age:", obj.age)
obj.age = 20
print("Jack's age changed:", obj.age)
del obj.age
# print(obj.age)

obj2 = People("Milk", 17)
print("Milk's age:", obj2.age)
obj2.age = 30
print("Milk's age changed:", obj2.age)
