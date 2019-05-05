#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

some_data = [1, 2, 3, 4, "1", "1", "2"]

count_dict = defaultdict(int)

for item in some_data:
    count_dict[item] += 1

print(count_dict)
