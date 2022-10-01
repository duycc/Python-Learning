# -*- coding: utf-8 -*-


# def logging(fn):
#     def inner(num1, num2):
#         print("-- computing --")
#         fn(num1, num2)

#     return inner


# @logging
# def sum_num(a, b):
#     result = a + b
#     print(result)


# sum_num(1, 2)


# def logging(fn):
#     def inner(num1, num2):
#         print("-- computing --")
#         result = fn(num1, num2)
#         return result

#     return inner


# @logging
# def sum_num(a, b):
#     result = a + b
#     return result


# result = sum_num(1, 2)
# print(result)


def logging(func):
    def inner(*args, **kwargs):
        print("-- computing --")
        func(*args, **kwargs)

    return inner


@logging
def sum_num(*args, **kwargs):
    result = 0
    for val in args:
        result += val

    for val in kwargs.values():
        result += val

    print(result)


sum_num(1, 2, a=10)
