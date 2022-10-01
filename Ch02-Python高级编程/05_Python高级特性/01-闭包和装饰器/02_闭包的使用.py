# -*- coding: utf-8 -*-


def config_name(name):
    def say_info(info):
        print(name + ": " + info)

    return say_info


tom = config_name("Tom")

tom("hello")
tom("hello world")


jerry = config_name("Jerry")
jerry("hello Tom")