"""
类方法装饰器： @classmethod  修饰的方法不需要实例化，
不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
"""


class TestDemo():
    def func(self,x,y):
        return x * y

    @classmethod
    def cfunc(cls,x,y):
        return x * y

if __name__=="__main__":

    print(TestDemo.cfunc(4,5))