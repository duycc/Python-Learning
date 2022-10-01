# -*- coding: utf-8 -*-


from unittest import result


def logging(flag):
    def decorator(func):
        def inner(num1, num2):
            if flag == "+":
                print("-- compute + --")
            elif flag == "-":
                print("-- compute - --")

            result = func(num1, num2)
            return result

        return inner

    return decorator


@logging("+")
def add(a, b):
    result = a + b
    return result


@logging("-")
def sub(a, b):
    result = a - b
    return result


print(add(1, 2))
print(sub(1, 2))
