"""
@property　特性装饰器
调用类中的方法时候可以引用类的属性。
被修饰的特性方法，内部可以实现处理逻辑，但对外提供统一的调用方式。
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