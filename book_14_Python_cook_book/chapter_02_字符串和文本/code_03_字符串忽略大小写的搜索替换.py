#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.I))
print(re.sub('python', 'snake', text, flags=re.I))


# 一个小缺陷, 替换的字符串并不会自动跟被匹配字符串的大小写保持一致
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.I))

