"""
正则表达式 - re模块

"""
import re

str = 'dog cat dog'

print(re.match('dog', str))     # 从字符串开头匹配，只匹配一项，返回一个match对象
print(re.match('cat', str))

print(re.search('dog',str))     # 从任意位置匹配，只匹配一项，匹配到第一个元素之后停止继续查找，返回一个match对象
print(re.search('cat', str))

print(re.findall('dog', str))   # 匹配所有不重复的对象，返回值一个列表

re_obj = re.compile(pattern='dog')    # 预编译返回一个正则表达式对象，具有跟re一样的属性和方法
print(re_obj.match(str))