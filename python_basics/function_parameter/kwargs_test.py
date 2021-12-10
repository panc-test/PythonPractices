"""
**kwargs参数：可接受任意个关键字参数，当函数调用时，所有未使用（未匹配）的关键字参数会在函数内组装进一个dict对象中，
此dict对象会赋值给变量名kwargs。

"""


# 自定义函数，只有**kwargs
def func(**kwargs):
    """
    **参数收集所有未匹配的关键字参数组成一个dict对象，局部变量kwargs指向此dict对象

    """
    print('kwargs类型：', type(kwargs))
    print('kwargs = ', kwargs)

# 调用函数，方法1
func(a=1, b=2)

# 调用函数，方法2，解包
dict = {'a': 1, 'b': 2}
func(**dict) # **参数用于解包dict对象的每个元素，作为一个一个的关键字参数传入到函数中

