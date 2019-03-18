#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing


def run(pname):
    print(pname)


def main():
    for i in range(10):
        p = multiprocessing.Process(target=run, args=('Process-' + str(i),))
        p.start()
        p.join()


if __name__ == '__main__':
    main()
