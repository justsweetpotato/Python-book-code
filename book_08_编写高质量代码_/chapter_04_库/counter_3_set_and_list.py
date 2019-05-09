#!/usr/bin/env python
# -*- coding: utf-8 -*-

some_data = [1, 2, 3, 3, "1", "1", "2"]

count_set = set(some_data)

count_list = []

for item in count_set:
    count_list.append((item, some_data.count(item)))

print(count_list)

