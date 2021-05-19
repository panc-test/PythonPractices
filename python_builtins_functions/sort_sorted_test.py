"""
1、sort是列表的内置方法，只作用于列表，直接修改原有的列表元素顺序，返回NONE。
2、sorted是python内置的一个排序函数，默认升序，适用于可迭代对象，返回一个新的可迭代对象。

"""

list = [2,5,4,3,1]

# list.sort()
# print(list.sort())
# print(list)

print(sorted(list))
print(list)
