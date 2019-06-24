#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = 'Today is 6/10/2019, PyCon starts 3/13/2013.'

new_text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

if __name__ == '__main__':
    print(text)
    print(new_text)
