"""
enumerate() 枚举函数，参数是一个可迭代对象，返回一个包含可迭代对象元素和索引下标的枚举对象
语法：
enumerate(iterable,start=0)
参数start指的是开始索引

"""
seq = ['one', 'two', 'three','four']

print(list(enumerate(seq)))
print(list(enumerate(seq, 5)))