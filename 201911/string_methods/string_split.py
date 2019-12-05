#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#split() 方法通过指定分隔符对字符串进行切片
# 语法：str.split(sep, count)
# sep -- 可选参数，指定的分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# count -- 可选参数，分割次数，默认为分隔符在字符串中出现的总次数。

str = "C语言\n中文网 >>> c.biancheng.net"
a=str.split()   # 以空格为分隔符，包含 \n
print(a)