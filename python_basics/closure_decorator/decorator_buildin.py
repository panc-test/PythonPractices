"""
Python内置装饰器:
@staticmethod 静态方法
1.不需要 self ,cls参数
2.可以直接通过类进行调用，也可以通过实例进行调用
3.调用方式：类名.方法名()

@classmethod 类方法
1.不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数
2.可以直接通过类进行调用，也可以通过实例进行调用
3.调用方式： 类名.方法名()

@property 特性装饰器
1.把类的方法伪装成属性调用的方式，就是把类里面的一个函数，变成一个属性一样的东西。
2.调用方式：实例名.方法名

"""


class TestDemo():

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def func1():  # 注意这里不带参数 self
        print('this is staticmethod')

    @classmethod
    def func2(cls):  # 注意这里带参数 cls
        print('this is classmethod')

    @property
    def func3(self):
        print('this is property')

    def func4(self):
        print('this is func4')
