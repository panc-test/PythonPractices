#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。语法：dict.update(dict2)

dict1={'one': 1, 'two': 2, 'three': 3}
dict2={'one':4, 'four': 9.3}
dict1.update(dict2)
print(dict1)

#可以看出在执行 update() 方法时，如果被更新的字典中己包含对应的键值对，那么原 value 会被覆盖；如果被更新的字典中不包含对应的键值对，则该键值对被添加进去。