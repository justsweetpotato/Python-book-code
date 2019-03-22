#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyperclip

from chapter_12_通过编程检测英文 import detectEnglish


# 欧几里得算法找出两个数的最大公约数
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


LIST_TEXT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(key):
    list_encrypt = ''

    for i in range(len(LIST_TEXT)):
        encrypt_number = (i * key + 5) % len(LIST_TEXT)
        list_encrypt += LIST_TEXT[encrypt_number]

    return list_encrypt


def crypt_text(msg, key, mode):
    charsA = LIST_TEXT
    charsB = encrypt(key)
    translated = ''

    if mode == 'encrypt':
        msg = msg.upper()
    elif mode == 'decrypt':
        charsA, charsB = charsB, charsA

    for word in msg:
        if word in charsA:
            word_index = charsA.find(word)
            translated += charsB[word_index]
        else:
            translated += word

    return translated


# 伪破译代码, 真实情况不会把加密方式 encrypt 暴露出来
def hack(msg):
    print("开始破译: {}...".format(msg[:100]))
    for i in range(20):
        print("正在尝试 Key #{}".format(i))
        answer = crypt_text(msg, i, 'decrypt')
        if detectEnglish.isEnglish(answer):
            print("key #{}: {}...".format(i, answer))
            print('破译完成! 是否继续, 回车继续, Q退出.')
            response = input('>')
            if response.strip().upper().startswith('Q'):
                return answer

    return None


if __name__ == '__main__':
    print(gcd(20, 8))
    # 如果两个数字的最大公约数是 1, 我们就说他们互质, 也就是如果 gcd(a, b) == 1, 则 a, b 互质.
    print(gcd(26, 9))

    key = 9
    list_encrypt = encrypt(key)
    print(LIST_TEXT)
    print(list_encrypt)
    # answer = hack('VV JLPPN ZNLPD! BJRT RT FXFXRFB!')
    # 在仿射加密法里，密钥A数字和符号集的大小必须互质。也就是说，gcd（密钥，符号集的大小）== 1。
    assert gcd(key, len(LIST_TEXT)) == 1, "Key Error! 无法破译仿射加密法!"
    answer = hack(crypt_text('CP HELLO WORLD! THIS IS AMAZING!', key, 'encrypt'))

    if answer == None:
        print('破译失败!')
    else:
        print('破译成功!')
        print(answer)
        pyperclip.copy(answer)
