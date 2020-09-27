"""
生成器:具有yield关键字的函数，yield可以理解为return，返回后面的值给调用者。
生成器常用方法：
1.close()方法：手动关闭生成器函数，后面的调用会直接返回StopIteration异常
2.__next__()方法：返回生成器的下一次调用
3.send()方法：接受外部传入的一个变量，并根据变量内容计算结果返回到生成器函数中
4.throw()方法：向生成器发送一个异常。

参考地址：
https://www.cnblogs.com/duwenxing/archive/2004/01/13/7396976.html
https://www.cnblogs.com/wj-1314/p/8490822.html

"""

def fun():
    """
    1、第一个__next__()方法的调用相当于启动生成器，运行到第一个yield处停止，跳出生成器函数。
    2、调用第二个__next__()方法后，从yield语句的下一条语句（16行）开始执行，直到重新运行到yield语句，执行后再次跳出生成器函数。
    3、超出迭代范围的时候抛出异常 StopIteration
    :return:
    """
    print("start")
    yield "Jack"
    print("continue")
    yield  "Pank"
    print("end")



f=fun()
print(f.__next__())
print("--------------------------------------------")
print(f.__next__())
print("--------------------------------------------")
print(f.__next__())

