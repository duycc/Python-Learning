# -*- coding: utf-8 -*-
import time

from black import main


def get_time(func):
    def inner():
        begin = time.time()
        func()
        end = time.time()
        print("func() cost time: {}".format(end - begin))

    return inner


@get_time
def func1():
    for i in range(100000):
        print(i)


func1()
