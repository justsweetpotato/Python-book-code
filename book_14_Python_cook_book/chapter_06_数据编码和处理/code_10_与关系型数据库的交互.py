#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

db = sqlite3.connect('database.db')
c = db.cursor()
# c.execute('create table portfolio (symbol text, shares integer, price real)')
# db.commit()
#
# stocks = [
#     ('GOOG', 100, 490.1),
#     ('AAPL', 50, 545.75),
#     ('FB', 150, 7.45),
#     ('HPQ', 75, 33.2),
# ]
#
# c.executemany('insert into portfolio values (?,?,?)', stocks)
# db.commit()


# c.execute('drop table portfolio')
# db.commit()


for row in c.execute('select * from portfolio'):
    print(row)
