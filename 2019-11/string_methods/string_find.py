#!/usr/bin/env python
# -*- coding:utf-8 -*-

#find() 方法用于检索字符串中是否包含目标字符串，如果包含，则返回第一次出现该字符串的索引；反之，则返回 -1。
# 语法:str.find(sub[,start[,end]])

str = "c.biancheng.net"
print(str.find('.'))
print(str.find('.',5,-1))

print(str.find('.',2,-4))

#rfind() 是从字符串右边开始检索到的第一个字符串索引
print(str.rfind('.'))