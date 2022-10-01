# -*- coding: utf-8 -*-


def make_div(func):
    """对被装饰的函数的返回值 div标签"""

    def inner(*args, **kwargs):
        return "<div>" + func() + "</div>"

    return inner


def make_p(func):
    """对被装饰的函数的返回值 p标签"""

    def inner(*args, **kwargs):
        return "<p>" + func() + "</p>"

    return inner


# 装饰过程: 1 content = make_p(content) 2 content = make_div(content)
# content = make_div(make_p(content))
@make_div
@make_p
def content():
    return "人生苦短"


result = content()

print(result)
