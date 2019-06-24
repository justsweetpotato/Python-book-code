#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryFile

with TemporaryFile('w+') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    print(data)

from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print(dirname)

from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w') as f:
    print(f.name)

import tempfile

print(tempfile.mkstemp())
print(tempfile.mkdtemp())
