"""
创建线程的方法一：
创建一个threading.Thread()对象，参数如下：
_init__(self, group=None, target=None, name=None,args=(), kwargs=None, *, daemon=None)
group：group参数必须为空，参数group是预留的，用于将来扩展；
target: 参数target是一个可调用对象（也称为活动[activity]），在线程启动后执行
name: 参数name是线程的名字。默认值为“Thread-N“，N是一个数字。
args：以元组的方式，为 target 指定的方法传递参数；
kwargs：以字典的方式，为 target 指定的方法传递参数；
daemon：指定所创建的线程是否为后代线程。

"""
import threading
import time


def run():
    """
    threading.current_thread().getName() 获取当前线程的名字,默认Thread-n格式
    如果创建线程组的时候参数name有值，则取指定的name值。
    :return:
    """
    print(threading.current_thread().getName(),time.ctime())
    time.sleep(1)
    print(threading.current_thread().getName(),time.ctime())
    time.sleep(1)
    print(threading.current_thread().getName(),time.ctime())
    time.sleep(1)
    print(threading.current_thread().getName(),time.ctime())
    time.sleep(1)

if __name__ == '__main__':
    """不带参数的线程 """
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()


    #也可以使用for方法来实现多个线程，也可以将多个线程放在一个列表中来遍历
    # for i in range(5):
    #     t=threading.Thread(target=function)
    #     t.start()


