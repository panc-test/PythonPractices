"""
all(iterable)  iterable 中的所有元素是否都均为真值（或可迭代对象为空），如果是返回 True，否则返回 False。
any(iyerable)  iterable 的任一元素为真值则返回 True。否则返回 False,如果可迭代对象为空，返回 False
注意：
元素除了是 0、空、None、False 外都算 True。

"""
print(all([1, 2, 3]))
print(all([0, 1, 2]))
print(all([]))  #可迭代对象为空
print('-------------------------------------')

print(any([1, 2, 3]))
print(any([0, 1, 2]))
print(any([]))
