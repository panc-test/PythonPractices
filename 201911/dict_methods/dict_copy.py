#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#通过 copy() 方法，可以将字典 a 的数据拷贝给字典 b。语法：b=a.copy
dict_a={'数学': 95, '语文': 89, '英语': 90}
print(dict_a)
dict_b=dict_a.copy()
print(dict_b)

#深拷贝，浅拷贝

