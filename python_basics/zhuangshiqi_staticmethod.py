"""
静态方法装饰器：@staticmethod 一个静态方法可以直接通过类进行调用，也可以通过实例进行调用

"""

class Demo():
    def func(self,x,y):
        return x * y

    @staticmethod
    def sfunc(x,y):
        return x * y


if __name__=="__main__":

    print(Demo.sfunc(6,5))
    print(Demo().sfunc(2,3))

