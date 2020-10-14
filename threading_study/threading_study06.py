"""
信号量（BoundedSemaphore类）：
信号量通常用于保护容量有限的资源
信号量管理一个内部计数器，该内部计数器随每个acquire()调用而递减，并随每个 调用而递增release()。
计数器永远不能低于零。当acquire() 发现它为零时，它将阻塞，直到其他线程调用为止 release()。
参考地址：https://www.cnblogs.com/chengd/articles/7770898.html

"""

import threading,time

#设置信号量的边界值
# semaphore = threading.Semaphore(5)
semaphore = threading.BoundedSemaphore(value=5)

def run():
    semaphore.acquire()   #加锁
    print(threading.current_thread().getName(),time.ctime())
    time.sleep(2)
    semaphore.release()    #释放

if __name__ == '__main__':
    for _ in range(10):
        t = threading.Thread(target=run)
        t.start()


"""
python多线程的缺陷：
1、GIL-全局解释器锁
2、无论系统CPU是几核的,只能使用一个来处理进程
https://www.cnblogs.com/xiangsikai/p/8178729.html

"""
