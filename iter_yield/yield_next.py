"""
生成器:
一种特殊的迭代器，使用yield而不是return语句返回结果。yield语句执行后，挂起函数的状态，以便下次从它离开的地方继续执行。
生成器常用方法：
1.__next__()方法：返回生成器的下一次调用
2.close()方法：手动关闭生成器函数，后面的调用会直接返回StopIteration异常
3.send()方法：接受外部传入的一个变量，并根据变量内容计算结果返回到生成器函数中
4.throw()方法：向生成器发送一个异常。

"""


def fun():
    print("start")
    yield "Jack"
    print("continue")
    yield "Pank"
    print("end")


"""
1、第一个__next__()方法，启动生成器，运行到第一个yield处(15行)停止，跳出生成器函数。
2、第二个__next__()方法，从16行开始执行，运行到下一个yield（17行）语句，再次跳出生成器函数。
3、超出迭代范围的时候抛出异常 StopIteration

"""

f = fun()
print(f.__next__())
# print(f.__next__())
# print(f.__next__())
