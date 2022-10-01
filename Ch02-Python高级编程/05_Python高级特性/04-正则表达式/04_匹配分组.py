# -*- coding: utf-8 -*-

import re

import re

# # 水果列表
# fruit_list = ["apple", "banana", "orange", "pear"]

# # 遍历数据
# for value in fruit_list:
#     # |    匹配左右任意一个表达式
#     match_obj = re.match("apple|pear", value)
#     if match_obj:
#         print("%s是我想要的" % match_obj.group())
#     else:
#         print("%s不是我要的" % value)

# match_obj = re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq|sina|yahoo)\.com", "hello@163.com")
# if match_obj:
#     print(match_obj.group())
#     # 获取分组数据
#     print(match_obj.group(1))
# else:
#     print("匹配失败")


# match_obj = re.match("(qq):([1-9]\d{4,10})", "qq:10567")

# if match_obj:
#     print(match_obj.group())
#     # 分组:默认是1一个分组，多个分组从左到右依次加1
#     print(match_obj.group(1))
#     # 提取第二个分组数据
#     print(match_obj.group(2))
# else:
#     print("匹配失败")

# match_obj = re.match("<[a-zA-Z1-6]+>.*</[a-zA-Z1-6]+>", "<html>hh</div>")

# if match_obj:
#     print(match_obj.group())
# else:
#     print("匹配失败")

# match_obj = re.match("<([a-zA-Z1-6]+)>.*</\\1>", "<html>hh</html>")

# if match_obj:
#     print(match_obj.group())
# else:
#     print("匹配失败")

# match_obj = re.match("<([a-zA-Z1-6]+)><([a-zA-Z1-6]+)>.*</\\2></\\1>", "<html><h1>www.itcast.cn</h1></html>")

# if match_obj:
#     print(match_obj.group())
# else:
#     print("匹配失败")

match_obj = re.match(
    "<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>",
    "<html><h1>www.itcast.cn</h1></html>",
)

if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
