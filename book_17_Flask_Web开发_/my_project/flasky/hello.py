#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World!</h1><br><p>Your browser is {}</p>'.format(user_agent)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
