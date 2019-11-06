#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#get() 函数返回指定键的值，如果值不在字典中返回默认值。语法：dict.get(key, default=None)

dict={'数学': 95, '语文': 89, '英语': 90}
print(dict.get('数学'))
print(dict.get('物理','没有这门学科'))