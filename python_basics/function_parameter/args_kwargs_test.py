"""
*args 参数：接受任意未使用的位置参数，类型元组
**kwargs 参数：接受任意未使用的关键字参数，类型字典

"""

# 自定义函数，包含*args和**kwargs
def func(argument, *args, **kwargs):
    print('argument = ', argument)
    print('args类型：', type(args))
    print('args = ',args)
    print('kwargs类型：', type(kwargs))
    print('kwargs = ',kwargs)

# 调用函数，方法1
# func(1, 2, 3, 4, a=1, b=2)

# 调用函数，方法2
tuple = (1, 2, 3, 4)
dict = {'a': 1, 'b': 2}
func(*tuple, **dict)  # 注意这里会把tuple解包出来的第一个实参1传给形参argument
