"""
迭代的好处：，
迭代是读取多少元素，就将多少元素装载到内存中，不读取就不装载，节省内存空间。

迭代器：
1、内置的可迭代对象：list, tuple, dict, set, str
2、内置 iter() 函数用来生成迭代器
3、自定义可迭代的类，含有__iter__()方法和__next__()方法

"""


list = [2,3,4]
print(type(list))
print(type(iter(list)))