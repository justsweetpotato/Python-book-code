#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyperclip


def encryptMessage(key, message):
    cipherText = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return ''.join(cipherText)


def main():
    myMessage = 'common sense is not so common.'
    myKey = 10  # 长度需限制为小于加密消息长度的一半
    cipherText = encryptMessage(myKey, myMessage)
    print(cipherText + '|')  # 为了避免末尾有空格难以辨认加上|
    pyperclip.copy(cipherText)


if __name__ == '__main__':
    main()
