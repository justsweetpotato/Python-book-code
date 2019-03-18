#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self


if __name__ == '__main__':
    x = Bunch(name="小张", position="学生")
    print(x.name)

    T = Bunch
    t = T(left=T(left="a", right="b"), right=T(left="c"))
    print(t.left)
    print(t.left.right)
    print(t.right.left)


