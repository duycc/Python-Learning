# -*- coding: utf-8 -*-

# 1. 生成器推导式
# d_generator = (i * 2 for i in range(5))
# print(d_generator)

# # val = next(d_generator)
# # print(val)

# for val in d_generator:
#     print(val)


# 2. yield关键词


def y_generator(n):
    for i in range(n):
        print("start generator...")
        yield i
        print("generator once...")


def fibnacci(num):
    x = 0
    y = 1

    curr_index = 0
    while curr_index < num:
        result = x
        x, y = y, x + y
        curr_index += 1
        yield result


def main():
    y = y_generator(5)
    # val = next(y)
    # print(val)

    # while True:
    #     try:
    #         val = next(y)
    #         print(val)
    #     except StopIteration as e:
    #         break
    # for i in y:
    #     print(i)

    fib = fibnacci(5)

    for val in fib:
        print(val)


if __name__ == "__main__":
    main()
