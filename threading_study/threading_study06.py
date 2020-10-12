"""
线程锁：
参考地址：https://blog.csdn.net/weixin_40481076/article/details/101594705

"""

import threading
from threading import Lock,Thread
import time,os

def work():
    global n
    lock.acquire()  #获取线程锁
    temp = n
    time.sleep(0.1)
    n = temp-1
    lock.release()  #释放线程锁

if __name__ == '__main__':
    lock = Lock()
    n = 100
    l = []
    for i in range(100):
        p = Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()
