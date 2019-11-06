#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#setdefault() 方法也用于根据 key 来获取对应 value 的值。

dict={'one': 1, 'two': 2, 'three': 3}
dict.setdefault('one',4)    #已有键值对不变
print(dict)
dict.setdefault('four',4)   #不存在的键值对加入字典中
print(dict)
