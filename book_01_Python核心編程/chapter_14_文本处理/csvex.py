#!/usr/bin/env python

import csv

DATA = (
    (9, 'Web Clients and Servers', 'base64, urllib'),
    (10, 'Web Programming: CGI & WSGI', 'cgi, time, wsgiref'),
    (11, 'Web Services', 'urllib, twython'),
)

print("*** WRITING CSV DATA")
with open('bookdata.csv', 'w') as f:
    writer = csv.writer(f)
    for record in DATA:
        writer.writerow(record)

print("*** REVIEW OF SAVED DATA")
with open('bookdata.csv', 'r') as f:
    reader = csv.reader(f)
    try:
        for chap, title, body in reader:
            print('Chapter %s: %r (featuring %s)' % (chap, title, body))
    except Exception as e:
        print(e)

