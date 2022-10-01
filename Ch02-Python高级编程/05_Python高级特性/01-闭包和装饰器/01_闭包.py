# -*- coding: utf-8 -*-


def func_out(num1):
    def func_inner(num2):
        result = num1 + num2
        print("sum = {}".format(result))

    return func_inner


f = func_out(1)
f(2)
f(3)
