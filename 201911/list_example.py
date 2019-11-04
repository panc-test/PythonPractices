#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#（1）创建列表

#方法1：
list1=["c.biancheng.net" , 1 , [2,3,4] , 3.0]   #列表可以存储整数、实数、字符串、列表、元组等任何类型的数据，并且和数组不同的是，在同一个列表中元素的类型也可以不同
print("list1=",list1)

#方法2：
range1=range(3,8)
list2=list(range1)
print("list2=",list2)

#访问列表
print(list1[0:3])

#删除列表：实际开始时，del 语句不常用，因为 Python 自带的垃圾回收机制会自动销毁不用的列表，所以即使开发者不手动将其删除，Python 也会自动将其回收。
name = name = ["C语言中文网","http://c.biancheng.net"]
print(name)
del name

