#!/usr/bin/env python
# -*- coding: utf-8 -*-

message = 'GUVF VF ZL FRPERG ZRFFNTR.'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num -= key

            if num < 0:
                num += len(LETTERS)
            translated += LETTERS[num]
        else:
            translated += symbol

    print('Key #{:<2d}: {}'.format(key, translated))

print('\n检查 Key #13.')
