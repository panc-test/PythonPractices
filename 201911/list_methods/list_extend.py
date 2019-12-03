#!/usr/bin/env python 
# -*- coding:utf-8 -*-


#extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。语法：listname.extend(obj)

list1=[1,3,'sd']
list2=(3,5)
list1.extend(list2)
print(list1)

#对比append（）方法