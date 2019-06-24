#!/usr/bin/env python
# -*- coding: utf-8 -*-
import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


if __name__ == '__main__':
    print(avg(777))
    print(avg(1, 2))
    print(avg(1, 2, 3, 4))

    print(make_element('item', 'Albatorss', size='large', quntity=6))
    print(make_element('p', '<spam>'))
