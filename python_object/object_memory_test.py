"""
对象内存地址，内存大小

"""
import sys

# 定义一个对象
class Person:
    pass

print("内存地址：",id(Person))
print("内存大小：",sys.getsizeof(Person))