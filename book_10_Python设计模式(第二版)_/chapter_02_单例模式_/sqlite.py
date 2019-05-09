#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
当存在多个 Web 应用程序时, 数据库连接池比实现单例要好的多
'''

import sqlite3


class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print(db1)
print(db2)
