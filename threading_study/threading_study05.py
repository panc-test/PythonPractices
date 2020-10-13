"""
递归锁：
互斥锁如果嵌套了多个锁之后，会将自己锁死永远都出不来了。
这个时候可以使用递归锁，它相当于一个字典，记录了锁的门与锁的对应值，当开门的时候会根据对应来开锁。

"""
import threading,time

# 生成递归锁实例
lock = threading.RLock()

# run1第二道锁
def run1():
    lock.acquire()
    print("run1",threading.current_thread().getName(),time.ctime())
    lock.release()

# run2第三道锁
def run2():
    lock.acquire()
    print("run2",threading.current_thread().getName(),time.ctime())
    lock.release()

# run3相当于第一道锁
def run3():
    lock.acquire()
    res = run1()
    time.sleep(1)
    print("run3",threading.current_thread().getName(),time.ctime())
    time.sleep(1)
    res2 = run2()
    lock.release()

# 循环开启10个线程
for i in range(10):
    t = threading.Thread(target=run3)
    t.start()
    t.join()
