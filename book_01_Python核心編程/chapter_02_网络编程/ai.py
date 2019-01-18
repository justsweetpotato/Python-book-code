#!/usr/bin/env python
import re
from random import choice


def fake_ai(msg):
    yes_or_no = ['是', '不是!']
    answer = ['我不知道你在说什么', '我无法回答你的问题', '这是什么?']

    if (msg == '你好') or ('晚上好' in msg) or ('早上好' in msg):
        return '你好, 很高兴见到你!'
    elif ('再见' in msg) or ('bye' in msg):
        return '好的, 祝你有个愉快的一天'
    elif ('谢谢' in msg) or ('谢谢你' in msg):
        return '不客气哦'
    elif ('hi' in msg) or ('hello' in msg):
        return 'hi'
    elif '是不是' in msg:
        return choice(yes_or_no)
    elif ('你' in msg) and ('吗' in msg):
        msg = re.sub('你', '我', msg)
        return msg.strip('吗?') + '!'
    elif '我' in msg:
        msg = re.sub('我', '你', msg)
        return msg.strip('吗?') + '!'
    elif '吗' in msg:
        return msg.strip('吗?') + '!'
    elif re.match(r'.{1,3}\?', msg):
        return msg.strip('?') + '!'
    elif ('好' in msg) or ('真' in msg) or ('太' in msg):
        return '谢谢!'
    else:
        return choice(answer)


if __name__ == '__main__':
    print('你好, 我是 Lucy.')
    while True:
        msg = input()
        f = fake_ai(msg)
        print(f)
        if (msg == '再见') or (msg == 'bye'):
            break
