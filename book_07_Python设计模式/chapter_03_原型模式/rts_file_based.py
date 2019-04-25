#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Knight(object):
    def __init__(self, level):
        self.unit_type = "Knight"

        filename = "{}_{}.dat".format(self.unit_type, level)

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\n" \
               "Life: {1}\n" \
               "Speed: {2}\n" \
               "Attack Power: {3}\n" \
               "Attack Range: {4}\n" \
               "Weapon: {5}\n".format(self.unit_type, self.life, self.speed, self.attack_power, self.attack_range,
                                      self.weapon)


class Barracks(object):
    def build_unit(self, unit_type, level):
        if unit_type == "knight":
            return Knight(level)


if __name__ == '__main__':
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    print("[knight1]\n{}".format(knight1))
g