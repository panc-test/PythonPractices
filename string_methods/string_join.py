#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#join() 方法也是非常重要的字符串方法，它是 split() 方法的逆方法，用来将列表（或元组）中包含的多个字符串连接成一个字符串。

# 语法：newstr = str.join(iterable)
# 参数：
# newstr：表示合并后生成的新字符串；
# str：用于指定合并时的分隔符；
# iterable：做合并操作的源字符串数据，允许以列表、元组等形式提供。

list1 = ['c', 'biancheng', 'net']
a='.'.join(list1)
print(a)