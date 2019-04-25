#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Soldier(object):
    def __init__(self, unit_type, level):
        self.unit_type = unit_type

        if self.unit_type == "Knight":
            if level == 1:
                self.life = 400
                self.speed = 5
                self.attack_power = 3
                self.attack_range = 1
                self.weapon = "short sword"

            elif level == 2:
                self.life = 600
                self.speed = 6
                self.attack_power = 6
                self.attack_range = 2
                self.weapon = "long sword"

        elif self.unit_type == "Archer":
            if level == 1:
                self.life = 200
                self.speed = 7
                self.attack_power = 1
                self.attack_range = 5
                self.weapon = "short bow"

            elif level == 2:
                self.life = 300
                self.speed = 8
                self.attack_power = 3
                self.attack_range = 10
                self.weapon = "long bow"

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
            return Soldier(unit_type.title(), level)

        elif unit_type == "archer":
            return Soldier(unit_type.title(), level)


if __name__ == '__main__':
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    archer1 = barracks.build_unit("archer", 2)
    print("[knight1]\n{}".format(knight1))
    print("[archer1]\n{}".format(archer1))
