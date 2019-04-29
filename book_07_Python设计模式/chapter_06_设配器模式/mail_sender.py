#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


def write_date():
    with open('users.csv', 'w') as f:
        f.write("name, surname, email\n")
        f.write("peter, potter, peter@gmail.com\n")


def read_date():
    with open('users.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        users = [row for row in reader]
    print(users)


if __name__ == '__main__':
    write_date()
    read_date()
