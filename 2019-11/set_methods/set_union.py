#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。语法：set.union(set1, set2...)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "runoob", "apple"}
set3=set1.union(set2)  #update函数没有返回结果，union函数有返回结果
print(set3)