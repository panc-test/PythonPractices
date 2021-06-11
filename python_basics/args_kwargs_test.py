"""
*args   元组
**kwargs    字典

"""


# #  只有*args
# def fun1(argument, *args):
#     print('argument = ', argument)
#     print('args类型：', type(args))
#     print(args)
#
#
# # 方法1
# fun1(1, 2, 3, 4)
# # 方法2
# tuple = (1, 2, 3, 4)
# fun1(*tuple)  # 解包


# # 只有**kwargs
# def fun2(argument, **kwargs):
#     print('argument = ', argument)
#     print('kwargs类型：', type(kwargs))
#     print(kwargs)
#
#
# fun2(1, a=1, b=2)
# dict = {'a': 1, 'b': 2}
# fun2(1, **dict)


# 包含*args和**kwargs
def fun3(argument, *args, **kwargs):
    print('argument = ', argument)
    print('args类型：', type(args))
    print(args)
    print('kwargs类型：', type(kwargs))
    print(kwargs)


fun3(1, 2, 3, 4, a=1, b=2)
tuple = (1, 2, 3, 4)
dict = {'a': 1, 'b': 2}
fun3(1,*tuple, **dict)
