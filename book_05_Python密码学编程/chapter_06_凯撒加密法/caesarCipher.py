#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyperclip

message = 'This is my secret message.'

key = 7

mode = 'encrypt'

LETTERS = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ [\\] ^_`a bcdefghijklmnopqrstuvwxyz{|}~'

translated = ''

# message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated += LETTERS[num]

    else:
        translated += symbol

print(translated)
pyperclip.copy(translated)  # 复制到剪切板

