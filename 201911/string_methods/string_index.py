#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#index() 方法也可以用于检索是否包含指定的字符串，不同之处在于，当指定的字符串不存在时，index() 方法会抛出异常。
# 语法：str.index(sub[,start[,end]])

str= "c.biancheng.net"
print(str.index('n',6))

# rindex() 方法，其作用和 index() 方法类似，不同之处在于它是从右边开始检索
print(str.rindex('n'))