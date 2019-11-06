#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#append() 方法用于在列表末尾添加新的对象。语法:listname.append(obj)

list1=[1,3,'sd']
list2=(3,5)
list1.append(list2)
print(list1)
list1.append('a')
print(list1)

#该方法无返回值，但是会修改原来的列表。
list3=list1.append(list2)
print(list3)

