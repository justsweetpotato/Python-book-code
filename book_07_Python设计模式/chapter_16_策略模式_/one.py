#!/usr/bin/env python
# -*- coding: utf-8 -*-

class StrategyExecutor(object):
    def __init__(self, strategy=None):
        self.strategy = strategy

    def execute(self, arg1, arg2):
        if self.strategy is None:
            print("Strategy not implemented...")
        else:
            self.strategy.execute(arg1, arg2)


class AdditionStrategy(object):
    def execute(self, arg1, arg2):
        print(arg1 + arg2)


class SubtractionStrategy(object):
    def execute(self, arg1, agr2):
        print(arg1 - agr2)


def main():
    no_strategy = StrategyExecutor()
    addition_strategy = StrategyExecutor(AdditionStrategy())
    subtraction_strategy = StrategyExecutor(SubtractionStrategy())

    no_strategy.execute(4, 6)
    addition_strategy.execute(4, 6)
    subtraction_strategy.execute(4, 6)


if __name__ == '__main__':
    main()
