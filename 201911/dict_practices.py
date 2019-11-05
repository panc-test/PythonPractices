#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#字典中添加键值对,语法：dict[key] = value  key与字典中现有的键都不同
dict1={'one': 1, 'two': 2, 'three': 3}
dict1['four']=4
print(dict1)

#字典中修改键值对，语法：dict[key] = value  key与字典中现有的键相同
dict2={'数学': 95, '语文': 89, '英语': 90}
dict2['数学']=99
print(dict2)

#字典中删除键值对,语法：del dict[key]
dict3={'数学': 95, '语文': 89, '英语': 90}
del dict3['数学']
print(dict3)

#判断字典中是否存在指定键值对，语法：key in/not in dict
dict4={'数学': 95, '语文': 89, '英语': 90}
print('数学'in dict4)
print('物理' in dict4)