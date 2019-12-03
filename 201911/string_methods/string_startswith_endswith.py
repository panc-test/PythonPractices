#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#startswith() 方法用于检索字符串是否以指定字符串开头，如果是返回 True；反之返回 False。
# 语法：str.startswith(sub[,start[,end]])
str = "c.biancheng.net"
print(str.startswith('c'))
print(str.startswith('a'))

#endswith() 方法用于检索字符串是否以指定字符串结尾，如果是则返回 True；反之则返回 False。
# 语法：str.endswith(sub[,start[,end]])

print(str.endswith('net'))
print(str.endswith('com'))
