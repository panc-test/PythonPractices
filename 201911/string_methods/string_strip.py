#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#strip()：删除字符串前后（左右两侧）的空格或特殊字符。
#lstrip()：删除字符串前面（左边）的空格或特殊字符。
#rstrip()：删除字符串后面（右边）的空格或特殊字符。
#这里的特殊字符指的是制表符（\t）、回车符（\r）、换行符（\n）等。

str = " c.biancheng.net\t\n\r"
print(str.strip())
print(str.lstrip())
print(str.rstrip())
