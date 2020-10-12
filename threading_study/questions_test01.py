"""
面试题：
1、https://www.163.com/上找3个接口
2、构建http请求
3、用多线程去调用这三个接口，每个接口各10次
4、打印出这三个接口中，平均响应时间最短的接口
5、打印出这30次请求中，时间最短和最多的2次请求id

"""

import requests
import threading

def api_test01():
    r = requests.get(url=None,params=None)

class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__()

    def run(self):
        pass

if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()