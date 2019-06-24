#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import Struct


def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]

    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)

    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)
