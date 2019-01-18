import os
import re


with os.popen('tasklist /nh', 'r') as f:  # /nh会去除每一行的标题
    for eachLine in f:
        print(re.findall(
            r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)', eachLine.strip()
        ))

