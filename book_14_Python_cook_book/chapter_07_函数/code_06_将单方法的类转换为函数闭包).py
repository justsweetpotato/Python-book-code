#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


douban = UrlTemplate('https://{type}.douban.com')
for line in douban.open(type='movie'):
    print(line.decode(), end='')


# ---------更简单----------
def url_template(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


douban = url_template('https://{type}.douban.com')
for line in douban(type='book'):
    print(line.decode(), end='')
