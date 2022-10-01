# -*- coding: utf-8 -*-

import re

# 1. ^
# 匹配以数字开头的数据
# match_obj = re.match("^\d.*", "3hello")
# if match_obj:
#     # 获取匹配结果
#     print(match_obj.group())
# else:
#     print("匹配失败")

# 2. $
# 匹配以数字结尾的数据
# match_obj = re.match(".*\d$", "hello5")
# if match_obj:
#     # 获取匹配结果
#     print(match_obj.group())
# else:
#     print("匹配失败")

# match_obj = re.match("^\d.*\d$", "4hello4")
# if match_obj:
#     # 获取匹配结果
#     print(match_obj.group())
# else:
#     print("匹配失败")

# 3. [^]
match_obj = re.match("[^aeiou]", "h")
if match_obj:
    # 获取匹配结果
    print(match_obj.group())
else:
    print("匹配失败")
