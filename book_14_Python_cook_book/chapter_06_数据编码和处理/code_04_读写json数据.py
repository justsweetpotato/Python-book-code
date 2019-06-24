#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}


json_str = json.dumps(data)
print(json_str)

data = json.loads(json_str)
print(data)

# with open('data.json', 'w') as f:
#     json.dump(data, f)
#
# with open('data.json', 'r') as f:
#     data = json.load(f)
#     print(data)