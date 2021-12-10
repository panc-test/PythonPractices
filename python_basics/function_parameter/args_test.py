"""
*args参数：可接受任意个位置参数，当函数调用时，所有未使用（未匹配）的位置参数会在函数内自动组装进一个tuple对象中，
此tuple对象会赋值给变量名args。

"""


# 自定义函数，只有*args
def func(*args):
    """
    *参数收集所有未匹配的位置参数组成一个tuple对象，局部变量args指向此tuple对象

    """
    print('args类型：', type(args))
    print('args=', args)


# 调用函数，方法1
func(1, 2, 3, 4)

# 调用函数，方法2，解包
tuple = (1, 2, 3, 4)
func(*tuple)    # *参数用于解包tuple对象的每个元素，作为一个一个的位置参数传入到函数中
