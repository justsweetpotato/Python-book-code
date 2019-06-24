#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

values = list(range(10))
print(random.choice(values))  # 随机选择一个元素
print(random.sample(values, 4))  # 提取 4 个不同元素
random.shuffle(values)  # 打乱元素的顺序
print(values)
print("生成随机整数:", random.randint(0, 10))
print("生成 0-1 范围的浮点数:", random.random())
print("获取 200 位的随机数:", random.getrandbits(200))