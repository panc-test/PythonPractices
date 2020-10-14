"""
函数式：将可调用对象传递给构造函数
创建一个threading.Thread()对象，参数如下：
*group*：group参数必须为空，参数group是预留的，用于将来扩展；
*target*: 参数target是一个可调用对象（也称为活动[activity]），在线程启动后执行
*name*: 参数name是线程的名字。默认值为“Thread-N“，N是一个数字。
*args*：传递给线程函数target的参数,他必须是个tuple类型.
*kwargs*：kwargs表示关键字参数。字典类型 {}.

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
    time.sleep(2)
    print(threading.current_thread().getName(),time.ctime())
    time.sleep(2)
    print(threading.current_thread().getName(),time.ctime())
    time.sleep(2)
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
    #     t=threading.Thread(target=test_thread)
    #     t.start()


