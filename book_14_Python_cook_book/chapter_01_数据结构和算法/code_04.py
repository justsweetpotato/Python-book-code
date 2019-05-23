#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

pairs = ((1, [1, 2]), (2, [3, 4, 5]), (3, 4))
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

print(d)
