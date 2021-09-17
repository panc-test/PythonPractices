"""
decorator.py是一个非常简单的装饰器加强包,你可以使用它自带的@decorator装饰器来完成你的装饰器。

"""
from datetime import datetime
from decorator import decorator

# 自定义一个logging装饰器
@decorator
def logging(func, *args, **kwargs):
    print("[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__))
    return func(*args, **kwargs)


@logging
def test():
    pass


if __name__ == '__main__':
    test()