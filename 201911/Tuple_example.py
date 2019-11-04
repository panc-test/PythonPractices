#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#toupe元组，有序的，不可修改，元组可以存储整数、实数、字符串、列表、元组等任何类型的数据，并且在同一个元组中，元素的类型可以不同

#（1）创建元组:当创建的元组中只有一个元素时，此元组后面必须要加一个逗号“,”，否则 Python 解释器会将其误认为字符串。
# 方法1：
tuple1=(2,3,4,'a')
print(tuple1)
print(type(tuple1))
# 方法2：
tuple2=tuple(range(1,5))
print(tuple2)

#（2）访问元组
print(tuple1[1])
print(tuple2[1:3])

#（3）修改元组
# 方法1：重新赋值
tuple3=(2,3,5)
print(tuple3)
tuple3=('a',3,5.7)
print(tuple3)
# 方法2：+
tuple4=tuple1+tuple2
print(tuple4)

#（4）删除元组
tuple5 = ('crazyit', 20, -1.2)
print(tuple5)
del(tuple5)

