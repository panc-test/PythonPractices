"""
Timer对象

"""
import threading

#实例化一个计时器
timer = threading.Timer

def hello():
    print("hello, world")

#10s后执行hello
t = timer(10, hello)
t.start()

