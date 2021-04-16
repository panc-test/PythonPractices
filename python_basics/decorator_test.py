"""
python 装饰器定义：
拓展其他函数功能的一种函数。在不用更改原函数代码的前提下给函数增加新的功能，
极大地复用了代码，让我们的代码更简短，也更Pythonic（Python范儿）
使用时，只需要的函数前加上@demo即可。

https://www.cnblogs.com/cicaday/p/python-decorator.html

"""
#装饰器函数
def debug(func):    # func 被装饰函数
    def wrapper():
        print("[DEBUG]: enter {}".format(func.__name__))    # func.__name__ 被装饰函数名称
        return func()
    return wrapper

#被装饰函数
@debug
def say_hello():
    print("hello!")


say_hello()






"""
#带参数的装饰器函数
def debug(func):
    def wrapper(*args,**kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args,**kwargs)
    return wrapper

@debug
def say_hello(eles):
    print("hello! {}".format(eles))

say_hello([1,2])

"""