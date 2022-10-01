# -*- coding: utf-8 -*-

import re

# 1. .
# ret = re.match(".", "M")
# print(ret.group())

# ret = re.match("t.o", "too")
# print(ret.group())

# ret = re.match("t.o", "two")
# print(ret.group())

# 2. []
# # 如果hello的首字符小写，那么正则表达式需要小写的h
# ret = re.match("h", "hello Python")
# print(ret.group())


# # 如果hello的首字符大写，那么正则表达式需要大写的H
# ret = re.match("H", "Hello Python")
# print(ret.group())

# # 大小写h都可以的情况
# ret = re.match("[hH]", "hello Python")
# print(ret.group())
# ret = re.match("[hH]", "Hello Python")
# print(ret.group())
# ret = re.match("[hH]ello Python", "Hello Python")
# print(ret.group())

# # 匹配0到9第一种写法
# ret = re.match("[0123456789]Hello Python", "7Hello Python")
# print(ret.group())

# # 匹配0到9第二种写法
# ret = re.match("[0-9]Hello Python", "7Hello Python")
# print(ret.group())

# ret = re.match("[0-35-9]Hello Python", "7Hello Python")
# print(ret.group())

# # 下面这个正则不能够匹配到数字4，因此ret为None
# ret = re.match("[0-35-9]Hello Python", "4Hello Python")
# # print(ret.group())

# 3. \d
# 普通的匹配方式
# ret = re.match("嫦娥1号", "嫦娥1号发射成功")
# print(ret.group())

# ret = re.match("嫦娥2号", "嫦娥2号发射成功")
# print(ret.group())

# ret = re.match("嫦娥3号", "嫦娥3号发射成功")
# print(ret.group())

# # 使用\d进行匹配
# ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
# print(ret.group())

# ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
# print(ret.group())

# ret = re.match("嫦娥\d号", "嫦娥3号发射成功")
# print(ret.group())

# 4. \D
# match_obj = re.match("\D", "f")
# if match_obj:
#     # 获取匹配结果
#     print(match_obj.group())
# else:
#     print("匹配失败")

# 5. \s

# 空格属于空白字符
# match_obj = re.match("hello\sworld", "hello world")
# if match_obj:
#     result = match_obj.group()
#     print(result)
# else:
#     print("匹配失败")


# # \t 属于空白字符
# match_obj = re.match("hello\sworld", "hello\tworld")
# if match_obj:
#     result = match_obj.group()
#     print(result)
# else:
#     print("匹配失败")


# 6. \S
# match_obj = re.match("hello\Sworld", "hello&world")
# if match_obj:
#     result = match_obj.group()
#     print(result)
# else:
#     print("匹配失败")


# match_obj = re.match("hello\Sworld", "hello$world")
# if match_obj:
#     result = match_obj.group()
#     print(result)
# else:
#     print("匹配失败")


# 7. \w
# 匹配非特殊字符中的一位
# match_obj = re.match("\w", "A")
# if match_obj:
#     # 获取匹配结果
#     print(match_obj.group())
# else:
#     print("匹配失败")


# 8. \W
match_obj = re.match("\W", "&")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")
