"""
@classmethod    类方法
实现直接用类调用函数方法，不必通过实例来调用类方法
1.不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数
2.修饰的方法不需要实例化，可以在类上调用，也可以在实例上调用
3.调用方式： 类名.方法名()

"""
class TestDemo():

    def __init__(self,*args,**kwargs):
        pass

    @classmethod
    def add(cls,x,y):   # 注意这里带参数 cls
        return x + y

# 类调用
print(TestDemo.add(4,5))

# 实例调用
demo = TestDemo()
print(demo.add(4, 5))
