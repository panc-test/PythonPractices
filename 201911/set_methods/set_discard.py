#!/usr/bin/env python 
# -*- coding:utf-8 -*-


# discard() 方法，此方法和 remove() 方法的用法完全相同，唯一的区别就是，当删除集合中元素失败时，此方法不会抛出任何错误。语法：set.discard(value)

set1={1,2,3,4}
set1.discard(3)
print(set1)

set1.discard(5)
print(set1)