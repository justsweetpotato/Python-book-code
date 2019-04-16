#!/usr/bin/env python
# -*- coding: utf-8 -*-

subnet = '10.0.10.0/24'
subnet_list = []


def add_subnet(subnet):
    temp_list = subnet.split(".")

    for i in range(256):
        temp_list[2] = str(i)
        subnet_list.append(".".join(temp_list))


def test_close(x):
    try:
        print(3 / x)
    except:
        pass
    finally:
        print("完成!")


if __name__ == '__main__':
    # print(subnet_list)
    # add_subnet(subnet)
    # print(subnet_list)
    test_close(0)
