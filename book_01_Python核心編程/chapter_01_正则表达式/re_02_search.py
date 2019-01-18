import re


m = re.search('foo', 'seafood')

if m is not None: print(m.group())
