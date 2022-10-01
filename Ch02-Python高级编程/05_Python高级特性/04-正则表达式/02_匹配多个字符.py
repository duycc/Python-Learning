# -*- coding: utf-8 -*-

import re

# 1. *
# ret = re.match("[A-Z][a-z]*", "M")
# print(ret.group())

# ret = re.match("[A-Z][a-z]*", "MnnM")
# print(ret.group())

# ret = re.match("[A-Z][a-z]*", "Aabcdef")
# print(ret.group())

# 2. +
# match_obj = re.match("t.+o", "two")
# if match_obj:
#     print(match_obj.group())
# else:
#     print("匹配失败")

# 3. ?
# match_obj = re.match("https?", "http")
# if match_obj:
#     print(match_obj.group())
# else:
#     print("匹配失败")

# 4. {}
ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
print(ret.group())

ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
print(ret.group())
