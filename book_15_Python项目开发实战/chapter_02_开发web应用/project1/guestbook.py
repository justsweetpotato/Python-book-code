# -*- coding: utf-8 -*-
import shelve
from flask import Flask, request, render_template, redirect, escape, Markup
from datetime import datetime

application = Flask(__name__)

DATA_FILE = 'guestbook.dat'


def save_data(name, comment, create_at):
    """保存提交的数据"""

    database = shelve.open(DATA_FILE)

    if 'greeting_list' not in database:
        greeting_list = []
    else:
        greeting_list = database['greeting_list']

    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'create_at': create_at,
    })

    database['greeting_list'] = greeting_list

    database.close()


def load_data():
    """返回已提交的数据"""

    database = shelve.open(DATA_FILE)
    greeting_list = database.get('greeting_list', [])
    database.close()

    return greeting_list


@application.template_filter('nl2br')
def nl2br_filter(s):
    """将换行符置换为 br 标签的模板过滤器"""

    return escape(s).replace('\n', Markup('<br>'))


@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    """格式化时间"""

    return dt.strftime('%m/%d/%Y %H:%M:%S')


@application.route('/')
def index():
    """首页，使用模板显示页面"""

    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)


@application.route('/post', methods=['POST'])
def post():
    """用于提交评论的 URL"""

    name = request.form.get('name')
    comment = request.form.get('comment')
    create_at = datetime.now()

    save_data(name, comment, create_at)

    return redirect('/')


if __name__ == '__main__':
    application.run('127.0.0.1', 8000, debug=True)
