# -*- coding: utf-8 -*-


def check(fn):
    def inner():
        print("please login first...")
        fn()

    return inner


# def comment():
#     print("comment...")


# comment = check(comment)
# comment()


# 语法糖装饰器
@check
def comment():
    print("comment...")


comment()
