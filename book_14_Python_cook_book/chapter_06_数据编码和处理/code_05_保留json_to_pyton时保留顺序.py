#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict

s = '{"name": "ACME", "shares": 50, "price": 490.1}'

data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)
