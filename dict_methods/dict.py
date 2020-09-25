#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#dict字典，无序，可变，键值对的形式，其中键是惟一的

#语法：dictname = {'key':'value1','key2':'value2',...,'keyn':valuen}

#（1）创建字典
#方法1：
dict1 = {'语文': 89, '数学': 92, '英语': 93}
print(dict1)
#方法2：使用 dict 字典类型提供的 fromkeys() 方法创建所有键值为空的字典，种创建方式，通常用于初始化字典，设置 value 的默认值。
knowledge = {'语文', '数学', '英语'}
dict2 = dict.fromkeys(knowledge)
print(dict2)
#方法3：
dict3=dict()    #空字典
print(dict3)

list1=['one','two','three']     #通过应用 dict() 函数和 zip() 函数，可将前两个列表转换为对应的字典。
list2=[1,2,3]
dict4=dict(zip(list1,list2))
print(dict4)

dict5= dict(one=11,two=12,three=13)
print(dict5)

#(3)访问字典
dict6={'one':4, 'two': 5, 'three': 6}
print(dict6['one'])   #通过键来访问对应的键值
print(dict6.get('one'))  #get方法来访问键值对
#为了防止在获取指定键的值时，因不存在该键而导致抛出异常，在使用 get() 方法时，可以为其设置默认值，这样，即便指定的键不存在，也不回报错
print(dict6.get('four','字典中无four键'))

#(4)删除字典
dict7={'one':14, 'two': 15, 'three': 16}
print(dict7)
del(dict7)