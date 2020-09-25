#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#update() 方法用于修改当前集合，可以添加新的元素或集合到当前集合中。语法：set.update(set)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "runoob", "apple"}
set1.update(set2)    #去掉重复的
print(set1)

set1.update('abc')      #和add方法的差异
print(set1)