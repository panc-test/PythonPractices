"""
正常情况下主线程要等待多线程的所有子线程都运行结束才会关闭
主线程：运行的py文件，一个进程
子线程：一个进程的多个线程，本例中的t1,t2

守护线程:所谓’线程守护’，就是主线程不管该线程的执行情况，只要是其他子线程结束且主线程执行完毕，主线程都会关闭。
也就是说:主线程不等待该守护线程的执行完再去关闭。

常见方法：
1、setDaemon(True)方法可以把子线程设置为主线程的守护线程，此方法必须在start之前
2、join()方法，让主线程等待子线程执行，此方法在start之后

"""

import threading
import time

def func1(a):
    for _ in range(8): #_下划线表示临时变量， 仅用一次，后面无需再用到
        print(a,time.ctime())
        time.sleep(1)

def func2(b):
    for  _ in range(3):
        print(b,time.ctime())
        time.sleep(1)

if __name__ == '__main__':
    """
    设置子线程t1为守护线程，主线程不等t1运行结束，只要其他的子线程t2运行结果，就会关闭主线程。
    """
    t1 = threading.Thread(target=func1,args=("线程1",))   #注意args参数类型是元组并以“，”结尾
    t2 = threading.Thread(target=func2,args=("线程2",))
    t1.setDaemon(True)  #设置主线程不等待子线程t1运行结束
    # t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()   ##设置主线程等待子线程t1运行结束
