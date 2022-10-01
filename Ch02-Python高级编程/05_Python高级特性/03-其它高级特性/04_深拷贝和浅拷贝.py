# -*- coding: utf-8 -*-

import copy

"""
不可变类型进行浅拷贝不会给拷贝的对象开辟新的内存空间，而只是拷贝了这个对象的引用。
"""
# a1 = 123123
# b1 = copy.copy(a1)
# c1 = a1

# print(id(a1))
# print(id(b1))
# print(id(c1))

# l1 = [1, 2]
# l2 = l1
# l3 = copy.copy(l1)
# print(id(l1))
# print(id(l2))
# print(id(l3))


"""
可变类型进行浅拷贝只对可变类型的第一层对象进行拷贝，对拷贝的对象会开辟新的内存空间进行存储，子对象不进行拷贝。
"""
# l4 = [1, 2, [3, 4]]
# l5 = l4
# l6 = copy.copy(l4)
# print(id(l4))
# print(id(l5))
# print(id(l6))

# print(id(l4[2]))
# print(id(l5[2]))
# print(id(l6[2]))

# l6[2].append(5)
# print(l4)
# print(l5)
# print(l6)

"""
不可变类型进行深拷贝如果子对象没有可变类型则不会进行拷贝，而只是拷贝了这个对象的引用，
否则会对该对象到最后一个可变类型的每一层对象就行拷贝, 对每一层拷贝的对象都会开辟新的内存空间进行存储
"""
# s1 = "hello python"
# s2 = s1
# s3 = copy.deepcopy(s1)
# print(id(s1))
# print(id(s2))
# print(id(s3))

# t1 = (1, ["duyong"])
# t2 = t1
# t3 = copy.deepcopy(t1)
# print(id(t1))
# print(id(t2))
# print(id(t3))

# print(id(t1[1]))
# print(id(t3[1]))

"""
可变类型进行深拷贝会对该对象到最后一个可变类型的每一层对象就行拷贝, 对每一层拷贝的对象都会开辟新的内存空间进行存储。
"""
l1 = [1, 2, [3, 4]]
l2 = l1
l3 = copy.deepcopy(l1)
print(id(l1))
print(id(l2))
print(id(l3))

print(id(l1[2]))
print(id(l3[2]))
