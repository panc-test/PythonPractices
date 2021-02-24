"""
map() 函数 :语法格式：map(function, iterable, ...)
说明：第二个参数 iterable 中的每一个元素去调用 function 函数，返回一个迭代器。

lambda 匿名函数: 语法格式 : lambda arguments : expression

"""
#将一个列表中的所有元素乘方
list = [1, 2, 3, 4]

#方法1 遍历
# map_list = map(lambda x : x **2,list)
# new_list = []
# for i in map_list:
#     new_list.append(i)
# print(new_list)

#方法2 列表推导式 格式： [表达式 for i in iterable if条件 ]
new_list = [i**2 for i in list]
print(new_list)