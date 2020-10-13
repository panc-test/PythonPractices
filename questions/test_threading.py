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


lock = threading.Lock()
time1 = []
time2 = []
time3 = []

#自定义多线程
class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.api1()
        self.api2()
        self.api3()

    def api1(self):
        r1 = requests.get(url='https://www.163.com/')
        time1.append(r1.elapsed.total_seconds())  #接口响应时间

    def api2(self):
        r2 = requests.get(url='https://c.m.163.com/nc/qa/uid.html')
        time2.append(r2.elapsed.total_seconds())  #接口响应时间

    def api3(self):
        r3 = requests.get(url='https://www.163.com/special/00774IVV/hot_pop_js2017.js?callback=latestInstantNews&d=1231')
        time3.append(r3.elapsed.total_seconds())  #接口响应时间


if __name__ == '__main__':
    for _ in range(10):
        t = MyThread()
        t.start()
        t.join()

    print('time1 = ',time1)
    print('time2 = ',time2)
    print('time3 = ',time3)

    time1_avg = sum(time1)/len(time1)   #接口1的平均响应时间
    time2_avg = sum(time2)/len(time2)
    time3_avg = sum(time3)/len(time3)

    print(time1_avg,time2_avg,time3_avg)
    print("最短平均响应时间=",min(time1_avg,time2_avg,time3_avg))