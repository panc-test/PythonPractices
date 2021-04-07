"""
线程锁-互斥锁
为什么要使用线程锁分析：https://blog.csdn.net/JackLiu16/article/details/81267176
互斥锁运行顺序分析：https://blog.csdn.net/weixin_40481076/article/details/101594705

"""
import threading,time

#实例化一个互斥锁对象
lock = threading.Lock()

def run():
    lock.acquire()  #获取锁
    print(threading.current_thread().getName(),time.ctime())
    time.sleep(5)
    lock.release()  #释放锁

for _ in range(10):
    t = threading.Thread(target=run)
    t.start()


