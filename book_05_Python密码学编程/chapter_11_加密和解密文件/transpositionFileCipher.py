#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, os, sys
from chapter_08_使用换位加密法加密 import transpositionEncrypt
from chapter_09_使用换位加密法解密 import transpositionDecrypt


def main():
    inputFilename = 'frankenstein.txt'
    # inputFilename = 'frankenstein.encrypted.txt'
    outputFilename = 'frankenstein.encrypted.txt'
    # outputFilename = 'frankenstein.decrypted.txt'
    myKey = 10
    myMode = 'encrypt'
    # myMode = 'decrypt'

    if not os.path.exists(inputFilename):
        print('The file {} does not exist. Quiting...'.format(inputFilename))
        sys.exit()

    if os.path.exists(outputFilename):
        print('This will overwrite the file {}. (C)ontinue or (Q)uit?'.format(outputFilename))
        response = input('>')
        if not response.lower().startswith('c'):
            sys.exit()

    # fileObj = open(inputFilename)
    # content = fileObj.read()
    # fileObj.close()
    with open(inputFilename, 'r') as f:
        content = f.read()

    print('{}sing...'.format(myMode.title()))

    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime)

    print('{}sion time: {} seconds'.format(myMode.title(), totalTime))

    # outputFileObj = open(outputFilename, 'w')
    # outputFileObj.write(translated)
    # outputFileObj.close()
    with open(outputFilename, 'w') as f:
        f.write(translated)

    print('Done {}sing {} ({} characters).'.format(myMode, inputFilename, len(content)))
    print('{}sed file is {}.'.format(myMode.title(), outputFilename))


if __name__ == '__main__':
    main()
