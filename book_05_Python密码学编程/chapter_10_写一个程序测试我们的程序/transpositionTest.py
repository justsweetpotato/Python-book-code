#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, sys
from chapter_08_使用换位加密法加密 import transpositionEncrypt
from chapter_09_使用换位加密法解密 import transpositionDecrypt


def main():
    random.seed(42)

    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test #{:>02d}: "{}..."'.format(i + 1, message[:50]))

        for key in range(1, len(message)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)
            if message != decrypted:
                print('Mismatch with key {} and message {}.'.format(key, message))
                print(decrypted)
                sys.exit()

    print('Transposition cipher test passed.')


if __name__ == '__main__':
    main()
