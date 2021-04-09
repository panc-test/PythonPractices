"""
dir(object) 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
help(object) 函数用于查看函数或模块用途的详细说明。

"""
print(dir())
print(dir('__builtins__')) #返回所有的内置函数
print(dir(list))

print(help(list))