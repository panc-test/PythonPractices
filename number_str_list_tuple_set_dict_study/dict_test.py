"""
python基础数据类型 ——字典 dict(可变的，无序的，可重复，键值对)
注意：
键值必须是惟一的，只能是数字、字符串、元组等不可变类型。列表等是可变的不能作为键

"""

"""
创建字典：
1.使用 {} 创建字典，键值对
2.使用 dict() 函数创建字典
3.使用 fromkeys() 方法创建字典
4.使用推导式
 
"""
# dict1 = {'数学': 95, '英语': 92, '语文': 84}
# print(dict1)

# 创建一个空字典
# dict1 = dict()
# print(dict1)

# 通过关键字dict和关键字参数创建
# dict1 = dict(one=1, two=2, three=3) # 不能带引号
# print(dict1)

# 通过二元组列表或者元组创建字典
# eles = [('one',1),('two',2),('three',3)]
# print(dict(eles))

# dict和zip函数结合创建字典
# keys = ['one', 'two', 'three']
# values = [1, 2, 3]
# dict1 = dict(zip(keys, values))
# print(dict1)

# fromkeys() 方法创建字典
# seq = ['one', 'two', 'three']
# val = 10
# dict1 = dict.fromkeys(seq,val)
# print(dict1)