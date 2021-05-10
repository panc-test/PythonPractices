"""
装饰器：拓展原函数功能的一种函数，返回值也是一个函数。

"""
# 通用装饰器
def funA(fun):     # 装饰器函数
    print("A")

    def innerA(*args,**kwargs):  # 接受原函数传参列表，元组，字典
        print(fun.__name__)    # 打印原函数名
        fun(*args,**kwargs)   # 运行原函数

    return innerA   # 闭包，外部函数返回值是内部函数

@funA
def funB():     # 原函数
    print("B")

# 注意这里 funB()函数没有return，默认return None
print(funB())
