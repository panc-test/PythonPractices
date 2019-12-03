#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#split() 方法可以实现将一个字符串按照指定的分隔符切分成多个子串，这些子串会被保存到列表中（不包含分隔符），作为方法的返回值反馈回来。
# 语法：str.split(sep,maxsplit)

str = "C语言中文网 >>> c.biancheng.net"
a=str.split()
print(type(a))
print(a)