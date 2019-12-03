#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
input() 函数用于获取用户输入的内容。由于 input() 函数总会将用户输入的内容放入字符串中，因此用户可以输入任何内容，input() 函数总是返回一个字符串。
'''

msg=input("请输入你的值：")
print(msg)
print(type(msg))