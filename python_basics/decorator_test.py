"""
装饰器
定义：
拓展原函数功能的一种函数，返回值也是一个函数。
特点：
在不改变原函数代码的前提下，给原函数增加新的功能，极大地复用了代码，让我们的代码更简短。使用时只需要在函数前加上@demo即可。

"""
#通用的装饰器
def debug(func):    # 装饰器函数
    def wrapper(*args,**kwargs):   # 接受列表，元组，字典
        print("[DEBUG]: enter {}".format(func.__name__))    # 装饰器函数的处理
        return func(*args,**kwargs)     # 被装饰函数的引用
    return wrapper

@debug
def test(eles):   # 被装饰函数
    print("hello {}".format(eles))

test("world")
