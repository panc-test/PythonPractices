"""
线程锁：线程的调度是由操作系统决定的，当t1、t2交替执行时,两个线程同时一存一取，就可能导致余额不对。
所以就有了线程锁，确保一个线程在修改balance的时候，别的线程一定不能改。
参考地址：https://blog.csdn.net/JackLiu16/article/details/81267176

"""

import threading,time

# 假定这是你的银行存款:
# balance = 0
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(1000000):
#         change_it(n)
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# 解决方案，添加线程锁
balance = 0
lock = threading.Lock()

def change_it(n):
    #先存后取，结果应该为0:
    """
    首先某个线程获取线程锁，开始执行代码段，其他进程等待。
    该线程执行完代码段之后，释放线程锁，其他线程获取该锁。
    """
    lock.acquire()
    global balance
    balance = balance + n
    balance = balance - n
    lock.release()

def run_thread(n):
    for i in range(10000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
