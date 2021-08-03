"""
格式化字符：
1.使用占位符 % 格式化
2.使用.format()方法格式化  ----python2.6
3.f-Strings表达式,可以解析任意类型的数据，运行的时候渲染，性能比%，.format()更好。python3.6

"""
# f"xxx" 表达式用法
name = 'peter'
age = 24
print(f"{name} is {age} years old")
print(F"{name} is {age} years old")
# 解析任意表达式
print(f'{1 + 2}')
print(f'{2 * 3}')
# 解析字符串方法
print(f'{name.upper()}')
# 解析列表，元组，字典
list = ['hello','world']
print(f'{list[0]}')
