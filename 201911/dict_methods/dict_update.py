#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#update() 方法可使用一个字典所包含的键值对来更新己有的字典。

dict1 = {'one': 1, 'two': 2, 'three': 3}
print(dict1)
dict1.update({'one':4.5, 'four': 9.3})
print(dict1)

#可以看出在执行 update() 方法时，如果被更新的字典中己包含对应的键值对，那么原 value 会被覆盖；如果被更新的字典中不包含对应的键值对，则该键值对被添加进去。