#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#title() 方法用于将字符串中每个单词的首字母转为大写，其他字母全部转为小写。
str1="c.biancheng.net"
print(str1.title())

#lower() 方法用于将字符串中的所有大写字母转换为小写字母。
str2="I LIKE YOU"
print(str2.lower())

#upper() 方法用于将字符串中的所有小写字母转换为大写字母。
str3="adbYU132"
print(str3.upper())
print('..................................')

#注意，以上 3 个方法都仅限于将转换后的新字符串返回，而不会修改原字符串。
print(str1)
print(str2)
print(str3)