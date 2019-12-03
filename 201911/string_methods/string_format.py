#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# format() 方法对字符串进行格式化。
# 语法：str.format(args)
# 其中 str 用于指定字符串的显示样式；args 用于指定要进行格式转换的项，如果有多项，之间有逗号进行分割。


#将1000000格式化成货币的形式
print('{:,d}'.format(1000000))