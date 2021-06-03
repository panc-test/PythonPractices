"""
linecache - 读取指定文件的指定行，常用来读取源码

"""
import linecache

# 读取源码
print(linecache.getline(linecache.__file__,3))

# 读取文件
print(linecache.getline(filename='file.txt',lineno=3))
print(linecache.getlines(filename='file.txt'))