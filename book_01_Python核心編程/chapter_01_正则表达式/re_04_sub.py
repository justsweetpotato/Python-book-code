import re


m = re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
print(m)

n = re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')  # subn返回一个元组, 替换后的字符换和替换数量
print(n)

