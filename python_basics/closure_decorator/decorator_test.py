"""
装饰器：拓展被装饰函数功能的一种函数，在不改变原函数的的基础上为函数添加新的功能，满足对拓展是开放的，对修改是封闭的原则。

"""


# 通用装饰器
def wrapper(func):  # 装饰器函数

    def inner(*args, **kwargs):  # 接受被装饰函数传参
        print('inner')
        return func(*args, **kwargs)  # 执行被装饰函数

    return inner  # 闭包，外部函数返回值是内部函数


@wrapper
def test():  # 被装饰函数
    print("test")


test()
# print(test())    # 注意这里 fun()函数没有return，默认return None
