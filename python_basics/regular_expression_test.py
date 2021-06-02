"""
正则表达式 - 语法

"""
# 匹配1-100内的任意数字
import random
import re

s = str(random.randint(1, 100))
print(s)
ret = re.match(r'(100|[1-9]\d{0,1})$',s)
print(ret.group())

