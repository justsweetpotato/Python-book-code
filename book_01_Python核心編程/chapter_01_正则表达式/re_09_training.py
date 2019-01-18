#!/usr/bin/env python
import re

from re_08_choiceredata import choice_data

# data = choice_data()
# print(data)
#
# patt_time = ' (\d+:\d+:\d+) '
# print("Time: " + re.search(patt_time, data).group(1))
#
# patt_email = '\w+@\w+\.(?:net|org|edu|com|gov)'
# print("Email: " + re.search(patt_email, data).group())
#
# patt_month = '\w+ (\w+)(?: |  )\d+ '
# print("Month: " + re.search(patt_month, data).group(1))
#
# patt_year = '\d+:\d+:\d+ (\d+):'
# print("Year: " + re.search(patt_year, data).group(1))
#
# patt_domain = '(\w+)@(\w+\.(?:net|org|edu|com|gov))'
# m = re.search(patt_domain, data)
# print("Name: " + m.group(1) + '\n' + "Domain: " + m.group(2))
#
# patt_my_email = '\w+@\w+\.(?:net|org|edu|com|gov)'
# print("My email: " + re.sub(patt_my_email, "justsweetpotato@gmail.com", data))
#
# patt_date = "\w+ (\w+)(?: |  )(\d+) \d+:\d+:\d+ (\d+)::"
# m = re.search(patt_date, data)
# print("Date: {},{},{}".format(m.group(1), m.group(2), m.group(3)))

# patt = '^(\w{3})'
# m = re.match(patt, data)
# if m is not None: print(m.group())
#
# patt = '.+(\d+-\d+-\d)'
# print(re.search(patt, data).group(1))

# data = "so, i hope you can bit me."
#
# patt = '[b|h][a|i|u|]t'
# print(re.search(patt, data).group())

# data = "My name is Jake Wong. He name is Sam Lee."
#
# patt = '[A-Z]\w+ [A-Z]\w+'
# print(re.findall(patt, data))

# data = "My name is Jake Wong, I like movies, and music."
#
# patt = ' (\w+), (\w+) '
# print(re.findall(patt, data))


# data = 'Python'
#
# patt = '^[A-Z|a-z|_][A-Z|a-z|\d|_]*'
# try:
#     m = re.match(patt, data).group()
# except Exception as e:
#     print("命名不合法!")
# else:
#     print(m)

# data = "https://www.google.eduwww.baidu.comwww.mahuateng.orgWWW.YAMAXUN.COM"
# patt = r'(?:http|https://)?www\.\w+\.(?:com|org|net|edu)'
# print(len(re.findall(patt, data, re.I)))

# data = "0."
# patt = "\d+\.(?:\d*)?"
# print(re.findall(patt, data))

# data = "ewar@gmail.come242@qq.comrkehjrw_ehwhka@ieowqjioqrq.com"
# patt = "[A-Za-z0-9_]+@[A-Za-z0-9]+\.com"
# print(re.findall(patt, data))

# data = "我们的电话号码是:589-333-3334,或者:(589)333-2451,333-2325."
# patt = "(?:(?:\d{3}-)|(?:\(\d{3}\)))?\d{3}-\d{4}"
# print(re.findall(patt, data))


