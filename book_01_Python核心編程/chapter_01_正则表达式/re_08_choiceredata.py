#!/usr/bin/env python

from random import choice

def choice_data():
    genList = []

    with open("redata.txt", "r") as f:
        while True:
            lines = f.readline()

            if lines == "":
                break
            else:
                genList.append(lines.strip())

    data = choice(genList)
    return data

if __name__ == '__main__':
    print(choice_data())
