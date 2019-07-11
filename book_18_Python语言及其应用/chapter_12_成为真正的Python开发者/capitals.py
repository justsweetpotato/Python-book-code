#!/usr/bin/env python
# -*- coding: utf-8 -*-

def process_cities(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if 'quit' == line.lower():
                return
            country, city = line.split(',')
            country = country.strip()
            city = city.strip()
            print(city.title(), country.title(), sep=',')


if __name__ == '__main__':
    import sys

    process_cities(sys.argv[1])
