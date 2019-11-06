#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#sort() 方法用于对列表元素进行排序，排序后原列表中的元素顺序会方发生改变。

#语法:listname.sort(key=None, reserse=False)

list = [3, 4, -2, -30, 14, 9.3, 3.4]
list.sort()
print(list)
list.sort(reverse=True)
print(list)