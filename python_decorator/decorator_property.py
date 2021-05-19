"""
@property　特性装饰器
把类的方法伪装成属性调用的方式，就是把类里面的一个函数，变成一个属性一样的东西。
调用方式：实例名.方法名

"""
class TestDemo():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    @property
    def add(self):
        return self.x + self.y

demo = TestDemo(4,5)
print(demo.add)     # 注意这里没有 ()