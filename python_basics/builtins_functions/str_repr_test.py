"""
str() 输出字符串，追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
repr() 输出字符串，追求明确性，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用。

"""
obj = "100"
print(str(obj))
print(repr(obj))


print(dir(obj))
print(obj.__repr__())
print(obj.__str__())