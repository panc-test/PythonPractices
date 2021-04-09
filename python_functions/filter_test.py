"""
filter() 函数用来过滤序列，
语法：filter(function, iterable)
注意：
返回符合条件的元素组成一个可迭代对象。

"""
#过滤列表中的所有奇数
lst = [1,2,3,4,5,6,7,8,9]
def func(n):
    return n % 2 ==1

new_list = list(filter(func, lst))
print(new_list)