"""
推导式:具有语言简洁，速度快等优点
列表推导式处理序列操作要比for循环高效

"""
"""
列表推导式
语法糖：[表达式 for循环 条件]
实例：返回一个列表中所有奇数的平方值组成的列表

"""
# list = [1, 2, 3, 4, 5]
# list1 = [i ** 2 for i in list if i % 2 == 1]
# print(list1)
# # 等价于
# list2 = []
# for i in list:
#     if i % 2 == 1:
#         list2.append(i ** 2)
#
# print(list2)


# # 去重
# list = [1,1,2,2,2,3,4,5,6,6,6]
# print([i for i in set(list)])





"""
元组推导式
实例：取出元组中的所有偶数组成一个新的元组

"""
# tup = (1, 2, 3, 4, 5)
# tup1 = (x for x in tup if x % 2 == 0)
# print(tup1)  # 注意元组推导式返回的是一个生成器对象
# print(tuple(tup1))



"""
集合推导式
实例：使用推导式生成集合

"""
set1 = {x for x in range(5)}
print(set1)


"""
字典推导式
实例：交换字典的键和值

"""
# dict = {'a': 1, 'b': 2, 'c': 3}
# dict1 = {value: key for key, value in dict.items()}
# print(dict1)