"""
math 模块:数学运算常用的函数
random 模块：生成随机数
"""
import math,random

print("python 内置函数：")
print("max() 函数返回给定参数的最大值==",max(1, 2, 3, 4, 5))
print("min() 函数返回给定参数的最小值==",min(1, 2, 3, 4, 5))
print("abs() 函数返回绝对值==",abs(-10))
print("round() 函数返回浮点数x的四舍五入值==",round(80.22333,1))

print("\n")
print("math 模块：")
print("fabs() 方法返回绝对值==",math.fabs(-10)) #fabs()函数只适用于float和integer类型，而abs()也适用于复数。
print("pow() 方法返回x**y的值==",math.pow(3,2))
print("exp() 方法返回e的x次幂==",math.exp(1))
print("ceil() 方法返回数字的上入整数==",math.ceil(10.2))
print("floor() 方法返回数字的下舍整数==",math.floor(10.2))
print("sqrt() 方法返回数字x的平方根==",math.sqrt(9))
print("modf() 方法返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示==",math.modf(10.2))

print("\n")
print("random 模块：")
print("random() 方法返回随机生成的一个实数，它在[0,1)范围内==",random.random())
print("choice() 方法返回一个列表，元组或字符串的随机项==",random.choice([1,2,3,4]))
print("uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内==",random.uniform(5,10))

