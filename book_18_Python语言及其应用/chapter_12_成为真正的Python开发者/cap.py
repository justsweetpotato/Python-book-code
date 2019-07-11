#!/usr/bin/env python
# -*- coding: utf-8 -*-

def just_do_it(text):
    if not isinstance(text, str):
        raise TypeError('value must be str')

    from string import capwords
    if text.startswith("\""):
        text = capwords(text[1:])
        text = "\"" + text
    else:
        text = capwords(text)
    return text

