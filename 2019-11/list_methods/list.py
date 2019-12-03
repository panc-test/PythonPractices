#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#list列表，有序，可变,元素不唯一可重复的

#（1）创建列表
#方法1：
list1=["c.biancheng.net" , 1 , [2,3,4] , 3.0,1]
print("list1=",list1)
#方法2：
range1=range(3,5)
list2=list(range1)
print("list2=",list2)

#（2）访问列表:切片
print(list1[3])
print(list1[0:3])

#(3)修改列表中的元素
list1[0]='a'
print('list1=',list1)
list1[2:]=[2,3]
print(list1)

#（4)删除列表：实际开始时，del 语句不常用，因为 Python 自带的垃圾回收机制会自动销毁不用的列表，所以即使开发者不手动将其删除，Python 也会自动将其回收。
name = name = ["C语言中文网","http://c.biancheng.net"]
print(name)
del name
#del方法根据目标元素所在位置的索引值进行删除
list4=[2,4,'gdsfd',5,3]
del list4[1]
print(list4)
del list4[1:3]
print(list4)


