# -*- coding: utf-8 -*-
def func_out(num1):
    def func_inner(num2):
        nonlocal num1
        num1 = 10
        result = num1 + num2
        print("result: {}".format(result))

    print(num1)
    func_inner(1)
    print(num1)

    return func_inner


f = func_out(1)
f(2)
