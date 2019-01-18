import re


m = re.match('foo', 'foo')

if m is not None:  # 这么做是为了防止没有返回值报错的情况
    print(m.group())



