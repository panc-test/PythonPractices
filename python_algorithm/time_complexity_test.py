"""
算法-时间复杂度
a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），求出所有a、b、c可能的组合。
https://www.cnblogs.com/Dr-wei/p/11857631.html

"""
import time


def get_time1():
    """
    使用三重循环用时904.6671814918518秒
    """
    start_time = time.time()
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                    print(a, b, c)
    end_time = time.time()
    print("用时time=", end_time - start_time)


def get_time2():
    """
    使用二重循环用时1.272592544555664秒
    """
    start_time = time.time()
    for a in range(1001):
        for b in range(1001):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
    end_time = time.time()
    print("用时time=", end_time - start_time)


if __name__ == '__main__':
    get_time1()
    # get_time2()
