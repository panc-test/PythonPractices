"""
格式化：
1.使用占位符 % 格式化，最初的
2.使用str.format()格式化，python2.6版本引入
3.f-strings表达式,可以解析任意类型的数据，运行的时候渲染，性能比%，.format()更好。python3.6版本引入

"""
name = 'peter'
age = 20
# %s 格式化字符串，%d 格式化整数
print('%s is %d years old' % (name, age))

# str.format() 三种写法,不限制参数类型，数量
print('{} is {} years old'.format(name, age))
print('{1} is {1} years old'.format(name, age))
print('{name} is {name} years old'.format(name='test', age=22))

# f-string表达式基本用法
print(f'{name} is {age} years old')
print(F'{name} is {age} years old')

# 解析表达式
print(f'{1 + 2}')
print(f'{2 * 4}')
# 解析内置函数
print(f'{name.upper()}')
# 解析基本数据类型的属性方法
list = ['hello', 'world']
print(f'{list[0]}')
