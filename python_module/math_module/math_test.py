"""
math 模块:数学运算常用的函数

"""
import math

print("fabs() 方法返回绝对值==",math.fabs(-10))
print("pow() 方法返回x**y的值==",math.pow(3,2))
print("exp() 方法返回e的x次幂==",math.exp(1))
print("ceil() 方法返回数字的上入整数==",math.ceil(10.2))
print("floor() 方法返回数字的下舍整数==",math.floor(10.2))
print("sqrt() 方法返回数字x的平方根==",math.sqrt(9))
print("modf() 方法返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示==",math.modf(10.2))