#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#ljust() 方法的功能是向指定字符串的右侧填充指定字符，从而达到左对齐文本的目的。语法：S.ljust(width[, fillchar])
s='abcdefgh'
addr='abcd'
print(s.ljust(10))
print(addr.ljust(10))

print(s.ljust(10,'-'))
print(addr.ljust(10,'-'))
print('...............................')


#rjust() 方法是向字符串的左侧填充指定字符，从而达到右对齐文本的目的。语法：S.rjust(width[, fillchar])
s='abcdefgh'
addr='abcd'
print(s.rjust(10))
print(addr.rjust(10))
print('...............................')

#center() 方法是让文本居中对齐。语法：S.center(width[, fillchar])
s='abcdefgh'
addr='abcd'
print(s.center(10))
print(addr.center(10))