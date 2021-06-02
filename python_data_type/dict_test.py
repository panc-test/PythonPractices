"""
python基础数据类型 ——字典 dict(可变的，无序的，键值对，键不能重复)
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


"""
访问字典：
1.dict[key] 键必须是存在的，否则会抛出异常。

"""
# dict1 = {'one':1,'two':2,'three':3}
# print(dict1['one'])
# print(dict1['four'])


"""
更新字典：
语法：dict[key] = values
对于已有的键，更新对于的值。没有键，增减键值对

"""
# dict1 = {'one':1,'two':2,'three':3}
# dict1['one'] = 0
# print(dict1)
# dict1['four'] = 4
# print(dict1)

"""
删除字典：
1.删除整个字典操作  del dict
2.删除字典中的键值对 del dict[key]
注意：
Python 自带垃圾回收功能，会自动销毁不用的字典，所以一般不需要通过 del 来手动删除。

"""
# dict1 = {'one':1,'two':2,'three':3}
# del dict1['one']
# print(dict1)
# del dict1
# print(dict1)


"""
字典添加键值对

"""
# dict1 = {"语文":80}
# dict1["数学"] = 95
# print(dict1)


"""
判断字典中是否存在指定的键
in 或者 not in

"""
# dict1 = {'数学': 95, '语文': 89, '英语': 90}
# print('数学' in dict1)
# print('物理' in dict1)


"""
字典的方法：
增：'update',
删：'pop', 'popitem',clear', 
改：'update', 
查：'keys', 'values','items', 'get','setdefault', 
其它：'copy', 'fromkeys', 

"""

"""
字典增加/修改元素：
1.update() 方法可以使用一个字典所包含的键值对来更新己有的字典。
语法：dict.update(dict2)
注意：
在执行 update() 方法时，如果被更新的字典中己包含对应的键值对，那么原 value 会被覆盖；
如果被更新的字典中不包含对应的键值对，则该键值对被添加进去。

"""
# dict1 = {'one': 1, 'two': 2, 'three': 3}
# dict2 = {'one': 0, 'four': 4}
# dict1.update(dict2)
# print(dict1)


"""
字典删除元素：
1.pop() 用来删除字典中指定的键值对。
2.popitem() 用来随机删除字典中一个键值对。
3.clear() 清空字典
注意：
其实，说 popitem() 随机删除字典中的一个键值对是不准确的，虽然字典是一种无须的列表，但键值对在底层也是有存储顺序的，
popitem() 总是弹出底层中的最后一个 key-value，这和列表的 pop() 方法类似，都实现了数据结构中“出栈”的操作。

"""
# dict1 = {'数学': 95, '语文': 89, '英语': 90, '化学': 83, '生物': 98, '物理': 89}
# dict1.pop('化学')
# print(dict1)
# dict1.popitem()     #实际删除的是最后一个键值对
# print(dict1)
# dict1.clear()
# print(dict1)


"""
字典查找元素：
1.keys() 方法用于返回字典中的所有键（key）
2.values() 方法用于返回字典中所有键对应的值（value）
3.items() 用于返回字典中所有的键值对（key-value）
注意：
它们的返回值不是列表或者元组类型，不能直接操作这几个方法的返回值。

"""
# scores = {'数学': 95, '语文': 89, '英语': 90}
# print(scores.keys())
# print(scores.values())
# print(scores.items())

# 将返回值转换成列表
# a = {'数学': 95, '语文': 89, '英语': 90}
# b = list(a.keys())
# print(b)

# 使用for循环遍历返回值
# a = {'数学': 95, '语文': 89, '英语': 90}
# for i in a.keys():
#     print(i)


"""
copy() 方法返回一个字典的拷贝，也即返回一个具有相同键值对的新字典
注意：
深拷贝，浅拷贝

"""
# a = {'one': 1, 'two': 2, 'three': [1,2,3]}
# b = a.copy()
# print(b)


"""
1.get() 方法返回指定键的值。
    语法：dict.get(key, default=None)
    若 key 存在，那么直接返回该 key 对应的 value；
    若 key 不存在，返回默认值 None ，或者设置的默认值。
2.setdefault() 方法返回指定键的值。
    语法：dict.setdefault(key, default=None)
    若 key 存在，那么直接返回该 key 对应的 value；
    若 key 不存在，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。
注意：
get和setdefault的区别，get方法不会修改原始的字典，setdefault方法会修改原始的字典。

"""
# dict1 = {'数学': 95, '语文': 89, '英语': 90}
# #key存在
# print(dict1.get('数学'))
# #key不存在，没有设置默认值
# print(dict1.get('物理'))
# #key存在，设置默认值
# print(dict1.get('化学',79))
# print(dict1)


# a = {'数学': 95, '语文': 89, '英语': 90}
# #key存在
# print(a.setdefault('数学'))
# print(a)
# #key不存在，不指定默认值
# print(a.setdefault('物理'))
# print(a)
# #key不存在，指定默认值
# print(a.setdefault('化学', 94))
# print(a)
