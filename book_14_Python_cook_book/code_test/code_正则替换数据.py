#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

msg_list = []

with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        res = re.findall('\d+\.\d+\.\d+\.\d+/\d+', line)
        if res:
            res = re.sub('(\d)/(\d{2})', r'\2', res[0])
            msg_list.append(res)
print(msg_list)

with open('test2.txt', 'w', encoding='utf-8') as f:
    for i in msg_list:
        f.write(i + '\n')
