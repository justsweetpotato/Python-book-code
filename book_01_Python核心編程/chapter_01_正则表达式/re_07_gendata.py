#!/usr/bin/env python
# 随机生成邮箱用于正则表达式匹配

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(maxsize)
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    # print('{}::{}@{}.{}::{}-{}-{}'.format(dtstr, login, dom, choice(tlds), dtint, llen, dlen))
    genStr = '{}::{}@{}.{}::{}-{}-{}'.format(dtstr, login, dom, choice(tlds), dtint, llen, dlen)
    print(genStr)

    with open("redata.txt", "a") as f:
        f.write(genStr)
        f.write("\n")
