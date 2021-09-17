"""
python基础数据类型——元组 tuple(不可变，有序的，可重复的)

"""

"""
创建元组
1.使用 () 创建
2.使用 tuple() 函数创建
注意：
当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号','，否则 Python 解释器会将它视为字符串。

"""
# tup1 = (1,2,3,4,2)
# tup2 = tuple('hello')
# print(tup1)
# print(tup2)


# tup1 = ('ab',)
# tup2 = ('ab')
# print(type(tup1))
# print(type(tup2))


"""
访问元组中的元素——索引，切片

"""
# tup = (0,1,2,3,4,5)
# print(tup[0])
# print(tup[1:5])

"""
删除元组 del

"""
# tup = (0,1,2,3,4,5)
# del tup
# print(tup)


"""
1.count() 方法用于统计某个元素在元组中出现的次数。
2.index() 方法用来查找某个元素在元组中首次出现的位置（也就是索引），如果该元素不存在，则会导致 ValueError 错误

"""
# tup = (1,1,3,2,3,4)
# print(tup.count(3))
# print(tup.index(5))