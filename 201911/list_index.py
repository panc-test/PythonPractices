#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#index() 方法用于定位某个元素在列表中出现的位置（也就是索引），如果该元素没有出现，则会引发 ValueError 错误。

#语法：listname.index(obj,start,end)

list = [2, 30, 'a', 'b', 'crazyit', 30]
print(list.index(30, 1,5))
