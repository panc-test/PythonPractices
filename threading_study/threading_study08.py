"""
Timer对象

"""
import threading


timer = threading.Timer
def hello():
    print("hello, world")

t = timer(10, hello)
# t.cancel()
t.start()  # after 10 seconds, "hello, world" will be printed

