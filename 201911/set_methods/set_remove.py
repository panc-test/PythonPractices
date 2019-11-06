#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# remove() 方法从set集合中删除元素,语法：setname.remove(element)
set1={1,2,3,4}
print(set1)
set1.remove(1)
print(set1)
# discard() 方法，此方法和 remove() 方法的用法完全相同，唯一的区别就是，当删除集合中元素失败时，此方法不会抛出任何错误。
set1.discard(3)
print(set1)
set1.discard(1)
print(set1)