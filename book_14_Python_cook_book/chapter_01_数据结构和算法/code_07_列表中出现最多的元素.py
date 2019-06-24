#!/usr/bin/env python
# -*- coding: utf-8 -*-

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter

word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(word_counts)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]
