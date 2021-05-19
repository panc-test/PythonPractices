"""
random 模块：生成随机数

"""
import random

print("random() 方法返回随机生成的一个实数，它在[0,1)范围内==",random.random())
print("choice() 方法返回一个列表，元组或字符串的随机项==",random.choice([1,2,3,4]))
print("uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内==",random.uniform(5,10))

