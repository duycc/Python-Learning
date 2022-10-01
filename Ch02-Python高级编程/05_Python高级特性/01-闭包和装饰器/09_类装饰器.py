# -*- coding: utf-8 -*-


class Check:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("please login first")
        self.__func()


@Check
def comment():
    print("comment...")


comment()
