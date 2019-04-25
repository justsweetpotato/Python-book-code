#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import randint

try:
    with open('point.txt', 'r') as f:
        content = f.readlines()
        height_point_name = content[0].strip()
        height_point = int(content[1].strip())
except:
    with open('point.txt', 'w') as f:
        f.write("None")
        f.write('\n')
        f.write('0')
        height_point_name = None
        height_point = 0

exit = False
point = 0

print("猜数字小游戏开始！随机生成了一个 100 以内的数字。（按 Enter 退出游戏）")
print("猜对加 5 分， 5 次或以内猜对加 10 分。")
print("目前世界记录为：{} 分。".format(height_point))
if height_point_name:
    print("记录创造者：{}".format(height_point_name))
print('-' * 50)


def auth():
    pass_count = 0
    while True:
        name = input("请输入用户名：")
        if name != '':
            break
        else:
            print("用户名不能为空!")

    if os.path.exists('{}.txt'.format(name)):
        with open('{}.txt'.format(name)) as f:
            real_password = f.readlines()[0].strip()
        while pass_count < 3:
            password = input("请输入密码: ")
            if password == real_password:
                print('-' * 50)
                print("欢迎回来， {}".format(name))
                return True, name
            else:
                pass_count += 1
                print("用户密码错误!")
        print("超过可尝试次数，退出...")
        return False, name
    else:
        while True:
            password = input("欢迎新用户！ 请设置你的密码： ")
            if password != '':
                with open('{}.txt'.format(name), 'a') as f:
                    f.write(password)
                    print('-' * 50)
                    print("欢迎你，{}".format(name))
                    return True, name
            else:
                print("密码不能为空！ ")


def main():
    global point
    global exit
    round = 1

    login, name = auth()
    if login:
        try:
            with open('{}.txt'.format(name), 'r') as f:
                self_point = f.readlines()[1].strip()
        except:
            self_point = 0
        print('你的历史最高分为：{}'.format(self_point))
        print('-' * 50)

        while True:
            count = 0
            content_list = []

            if exit == True:
                print("你的分数是：{}".format(point))
                if point > int(self_point):
                    print("你超过了自己的记录！")
                    with open('{}.txt'.format(name), 'r') as f:
                        content = f.readlines()
                        for msg in content[:]:
                            msg = msg.strip('\n')
                            content_list.append(msg)
                        if len(content_list) > 1:
                            content_list[1] = str(point)
                        else:
                            content_list.append(str(point))

                    with open('{}.txt'.format(name), 'w') as f:
                        f.write('\n'.join(content_list))
                if point > height_point:
                    print("你创造了新世界记录！")
                    with open('point.txt', 'w') as f:
                        f.write(name)
                        f.write('\n')
                        f.write(str(point))
                break

            num = randint(1, 101)

            while True:
                try:
                    response = int(input("请输入数字："))
                except:
                    exit = True
                    break
                if response < num:
                    count += 1
                    print("小了")
                elif response > num:
                    count += 1
                    print("大了")
                else:
                    count += 1
                    round += 1
                    print("对了，正确数字是：{}，你尝试了：{} 次。".format(num, count))
                    print("开始第 {} 轮，或按 Enter 退出游戏。".format(round))
                    if count <= 5:
                        point += 10
                    else:
                        point += 5
                    break

    else:
        print("用户认证失败！")


if __name__ == '__main__':
    main()
