import re


s = 'This and that.'

m = re.findall(r'(th\w+) and (th\w+)', s, re.I)
print(m)

n = re.finditer(r'(th\w+) and (th\w+)', s, re.I)  # 返回一个迭代器列表
for i in n:
    print(i.groups())

[print(i.groups()) for i in re.finditer(r'(th\w+) and (th\w+)', s, re.I)]

