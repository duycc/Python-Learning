# -*- coding: utf-8 -*-

# 1. 装饰器方式
# class Person:
#     def __init__(self):
#         self.__age = 0

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, new_age):
#         if new_age > 0 and new_age < 150:
#             self.__age = new_age


# p = Person()
# print(p.age)
# p.age = 100
# print(p.age)

# 2. 类属性方式
class Person:
    def __init__(self) -> None:
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0 and new_age < 150:
            self.__age = new_age

    age = property(get_age, set_age)


p = Person()
print(p.age)
p.age = 100

print(p.age)
