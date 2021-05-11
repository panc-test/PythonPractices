"""
python基础数据类型——集合 set(可变，无序的，不重复)
集合方法：
增：add,update
删：pop,remove,dicard,clear
改：无
查：无（集合是无序的）
其它：copy,union等

"""

"""
创建集合：
1.使用 {} 创建
2.使用 set() 函数创建
注意：
如果要创建空集合，只能使用 set() 函数实现。因为直接使用一对 {}，Python 解释器会将其视为一个空字典。

"""
# set1 = {1,2,3,4,5}
# set2 = set(range(5))
# set3 = set()
# print(set1)
# print(set2)
# print(set3,type(set3))

"""
访问集合中的元素:
1.使用for循环
注意：
由于集合中的元素是无序的，因此无法向列表那样使用下标访问元素。

"""
# set1 = {1,2,3,4,5}
# for ele in set1:
#     print(ele)


"""
删除集合 del

"""
# set1 = {1,2,3,4,5}
# del set1
# print(set1)



"""
集合运算——运算符

"""
# set1 = {1,2,3}
# set2 = {3,4,5}
# #交集
# print(set1 & set2)
# #并集
# print(set1 | set2)
# #差集
# print(set1 - set2)
# #对称差集
# print(set1 ^ set2)


"""
集合方法：
增：add,update
删：remove,dicard,pop
改：无
查：无（集合是无序的）
其它：clear,copy,union等

"""

"""
集合添加元素：
1.add() 方法，如果添加的元素在集合中已存在，则不执行任何操作。格式 ：set.add()
2.update() 方法,如果添加的元素在集合中已存在，则不执行任何操作。格式 ：set.update()
注意： 
add () 方法参数只能是数字、字符串、元组或者布尔类型（True 和 False）值，
不能添加列表、字典、集合这类可变的数据，否则 Python 解释器会报 TypeError 错误。
update() 方法参数列表，字典，集合都可以

"""
# # add()
# set1 = {1,2,3}
# set1.add(1)
# print(set1)
# set1.add(4)
# print(set1)

# update()
set1 = {1,2,3,4}
set1.update([1,5],[2,5])    #多个列表用逗号隔开
print(set1)


"""
集合删除元素：
1.pop() 方法随机移除集合的一个元素，并返回移除的元素
2.remove() 方法移除指定的元素    
3.discard() 方法移除指定的元素 
4.clear() 方法清除集合中的元素
注意：
如果被删除元素本就不包含在集合中，remove会抛出 KeyError 错误。discard不抛异常。

"""
# #pop()
# set1 = {1,2,3,4,5}
# ele = set1.pop()
# print(ele)
# print(set1)

# set1 = {1,2,3,4,5}
# set1.remove(1)
# print(set1)
# # set1.remove(0)
# set1.discard(0)
# print(set1)

# # clear()
# set1 = {1,2,3,4,5}
# set1.clear()
# print(set1)



"""
其它方法：
copy() 方法拷贝集合元素

"""
# set1 = {1,2,3,4,5}
# set2 = set1.copy()
# print(set2)


"""
集合运算的方法
1.union() 方法,返回并集
2.intersection() 方法，返回交集
3.difference() 方法，返回差集

"""
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set.union(set1, set2))
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))

