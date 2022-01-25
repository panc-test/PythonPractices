"""
Python内置装饰器:
@staticmethod 静态方法
1.不需要 self ,cls参数
2.调用方式：类名.方法名()

@classmethod 类方法
1.cls做为方法的第一个参数，隐式的将类做为对象传递给方法，调用时无须实例化。
2.调用方式：类名.方法名()

@property 类属性
1.使调用类中的方法像引用类中的字段属性一样。被修饰的特性方法，内部可以实现处理逻辑，但对外提供统一的调用方式。
2.调用方式：实例名.方法名，注意不加()

"""


class TestDemo():

    def __init__(self, *args, **kwargs):  # 使用 *args,**kwargs实现构造函数的多态性
        pass

    @staticmethod
    def func1():  # 注意这里不带参数 self
        print('this is staticmethod')

    @classmethod
    def func2(cls):  # 注意这里带参数 cls
        print('this is classmethod', cls)

    @property
    def func3(self):
        str = 'this is property'
        return str

    def func4(self):
        print('this is func4', self)


if __name__ == '__main__':
    # 实例化对象
    testdemo = TestDemo()
    print(TestDemo)
    print(testdemo)
    TestDemo.func1()
    TestDemo.func2()
    print(testdemo.func3)
    testdemo.func4()
