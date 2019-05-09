#!/usr/bin/env python
# -*- coding: utf-8 -*-

class EventManager(object):
    def __init__(self):
        print("会务经理: 让我去办这些事\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


class Hotelier(object):
    def __init__(self):
        print("正在为婚礼预定酒店 --")

    def __isAvailable(self):
        print("酒店今天免费吗?")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("预定成功\n\n")


class Florist(object):
    def __init__(self):
        print("正在为婚礼准备鲜花 --")

    def setFlowerRequirements(self):
        print("玫瑰已经准备好.\n\n")


class Caterer(object):
    def __init__(self):
        print("正在联系餐饮服务商 --")

    def setCuisine(self):
        print("食物已准备完毕\n\n")


class Musician(object):
    def __init__(self):
        print("正在准备音乐 --")

    def setMusicType(self):
        print("音乐准备完毕\n\n")


class You(object):
    def __init__(self):
        print("你: 哇! 准备婚礼??!")

    def askEventManager(self):
        print("你: 我去找会务经理.\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("你: 谢谢你会务经理, 所有事项都完成了!")


you = You()
you.askEventManager()
