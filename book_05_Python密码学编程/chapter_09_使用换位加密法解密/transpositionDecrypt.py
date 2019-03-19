#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, pyperclip


def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)  # ceil函数 向上取整
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plainText = [''] * numOfColumns

    col, row = 0, 0

    for symbol in message:
        plainText[col] += symbol
        col += 1

        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plainText)


def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8
    plainText = decryptMessage(myKey, myMessage)
    print(plainText + '|')
    pyperclip.copy(plainText)


if __name__ == '__main__':
    main()
