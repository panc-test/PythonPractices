"""
事件对象 threading.Event
set()	将“Flag”设置为True
clear()	将“Flag”设置为False
wait()	如果“Flag”值为 False，主线程就会阻塞；如果“Flag”值为True，主线程不再阻塞。
isSet() 判断“Flag”值是否为True。

"""

import threading
import time

#实例化一个事件对象
event = threading.Event()

def run():
    while not event.isSet():
        print(threading.current_thread().getName(), time.ctime())
        time.sleep(5)
    event.wait(timeout=10)  # 阻塞线程，为什么timeout=10没起到作用

if __name__ == '__main__':
    #使用多线程去调用run
    for i in range(10):
        th = threading.Thread(target=run)
        th.start()
    #阻塞30s后运行主线程
    time.sleep(30)
    event.set()




