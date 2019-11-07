#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#count 方法用于检索指定字符串在另一字符串中出现的次数，如果检索的字符串不存在，则返回 0，否则返回出现的次数。

# count 方法的语法格式如下：
# str.count(sub[,start[,end]])
#
# 此方法中，各参数的具体含义如下：
# str：表示原字符串；
# sub：表示要检索的字符串；
# start：指定检索的起始位置，也就是从什么位置开始检测。如果不指定，默认从头开始检索；
# end：指定检索的终止位置，如果不指定，则表示一直检索到结尾。


str1 = "c.biancheng.net"
a=str1.count('.')
print(a)

b=str1.count('1')
print(b)

c=str1.count('.',1,4)
print(c)