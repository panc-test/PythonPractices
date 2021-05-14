"""
@staticmethod   静态方法
可以直接通过类进行调用，也可以通过实例进行调用
不需要 self ,cls参数
调用方式：类名.方法名()

"""
class TestDemo():

    def __init__(self,*args,**kwargs):
        pass

    @staticmethod
    def add(x,y):   # 注意这里不带参数 self
        return x + y

# 类调用
print(TestDemo.add(4, 5))

# 实例调用
demo = TestDemo()
print(demo.add(4, 5))


