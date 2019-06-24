#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

with  open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)
    for row in f_csv:
        print(row)

print('-' * 50)

from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row)

print('-' * 50)

with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)