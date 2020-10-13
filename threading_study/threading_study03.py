"""
守护线程:
主线程不管守护线程的执行情况，只要是其他子线程结束且主线程执行完毕，主线程都会关闭。

常见方法：
1、setDaemon(True)方法可以把子线程设置为主线程的守护线程，此方法必须在start之前
2、join()方法，让主线程等待子线程执行，此方法在start之后

"""

import threading
import time

def run1(name,n):
    for _ in range(n): #_下划线表示临时变量， 仅用一次，后面无需再用到
        print(name,time.ctime())
        time.sleep(1)

def run2(name,n):
    for _ in range(n):
        print(name,time.ctime())
        time.sleep(1)

if __name__ == '__main__':
    """
    设置子线程t1为守护线程，主线程不等t1运行结束，只要其他的子线程t2运行结果，就会关闭主线程。
    """
    t1 = threading.Thread(target=run1,args=("线程1",10,))   #注意args参数类型是元组并以“，”结尾
    t2 = threading.Thread(target=run2,args=("线程2",5,))
    t1.setDaemon(True)  #设置t1为守护线程
    t1.start()
    t2.start()
    # t1.join()   ##设置主线程等待子线程t1运行结束
