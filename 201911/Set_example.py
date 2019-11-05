#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#集合是无序的，可变的，元素都是唯一的，互不相同

#(1)创建集合
#方法1：
set1={1,'c',1,(1,2,3),'c'}
print(set1)
#方法2：set()函数，语法：setname = set(iteration),其中，iteration 就表示字符串、列表、元组、range 对象等数据。
list=[1,2,3,4,5,4]
print(list)
set2 = set(list)
print(set2)


#(2)访问集合：由于集合中的元素是无序的，因此无法向列表那样使用下标访问元素。Python 中，访问集合元素最常用的方法是使用循环结构，将集合中的数据逐一读取出来。
set3= {1,'c',1,(1,2,3),'c'}
for ele in set3:
    print(ele)

#(3)删除集合
a = {1,'c',1,(1,2,3),'c'}
print(a)
del(a)

