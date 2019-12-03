#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。语法:listname.sort(key=None, reserse=False)

list = [3, 4, -2, -30, 14, 9.3, 3.4]
list.sort()
print(list)

#key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
#reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
list2=[5,3.0,1,-3]
list2.sort(reverse=True)
print(list2)

