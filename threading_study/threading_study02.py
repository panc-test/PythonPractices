"""
自定义线程：继承threading.Thread来定义线程类，然后重写__init__方法和run方法
start 和 run方法的区别
参考地址：https://www.cnblogs.com/yoyoketang/archive/2004/01/13/8308863.html
https://blog.csdn.net/weixin_40481076/article/details/101594705

"""
import threading
import time

class MyThread(threading.Thread):

    def __init__(self,name):    #重写__init__方法,可以使用super来调用父类的方法
        # super().__init__()
        threading.Thread.__init__(self)
        self.name = name

    def run(self):   #重写run方法，注意方法名只能是 run
        print("开始线程",self.name, time.ctime())
        time.sleep(2)
        print("干活中",self.name, time.ctime())
        time.sleep(2)
        print("结束线程",self.name, time.ctime())


if __name__ == '__main__':
    t1 = MyThread(name='线程1')
    t2 = MyThread(name='线程2')
    t1.start()
    t2.start()

