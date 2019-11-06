#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。语法：dict.fromkeys(seq[, value])

seq=('数学','语文','英语')
dict1=dict.fromkeys(seq)
dict2=dict.fromkeys(seq,90)
print(dict1)
print(dict2)