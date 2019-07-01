#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections.abc
import bisect


class SortedItems(collections.abc.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)
        # self._items.append(item)
        # self._items = sorted(self._items)


items = SortedItems([5, 1, 3])
print(list(items))
print(items[0], items[-1])
items.add(2)
print(list(items))

items = SortedItems()
print(isinstance(items, collections.abc.Iterable))
print(isinstance(items, collections.abc.Sequence))
print(isinstance(items, collections.abc.Container))
print(isinstance(items, collections.abc.Sized))
print(isinstance(items, collections.abc.Mapping))


class Items(collections.abc.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)


a = Items([1, 2, 3])
print(len(a))
a.append(2)
print(a.count(2))
a.remove(3)