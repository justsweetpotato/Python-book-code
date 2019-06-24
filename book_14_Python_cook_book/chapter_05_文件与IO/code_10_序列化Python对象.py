#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

data = {'name': 'jack', 'age': 19}

f = open('data.txt', 'wb')
pickle.dump(data, f)
f.close()

s = pickle.dumps(data)
print(s)

f = open('data.txt', 'rb')
data = pickle.load(f)
print(data)
f.close()

data = pickle.loads(s)
print(data)
