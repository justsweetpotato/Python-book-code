#!/usr/bin/env python
# -*- coding: utf-8 -*-

some_data = [1, 2, 3, 4, 5, 5, "1", "1", "2"]

count_dict = {}

for item in some_data:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)
