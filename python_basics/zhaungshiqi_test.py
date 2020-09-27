"""
装饰器：装饰器本质上是一个Python函数，在不改变任何代码的情况下为已经存在的对象添加额外的功能，极大地复用了代码。
常见装饰器；内置装饰器；类装饰器、函数装饰器、带参数的函数装饰器
参考地址：https://www.cnblogs.com/arvin-feng/p/11108799.html

"""
#函数装饰器
def use_logging(func):
  print("%s is running" % func.__name__)
  return func

@use_logging
def bar():
  print('i am bar')

#装饰器相当于执行了装饰函数use_loggin后又返回被装饰函数bar,因此bar()被调用的时候相当于执行了两个函数。等价于use_logging(bar)()
bar()
