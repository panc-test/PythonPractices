"""
time 时间模块
1.时间格式（时间戳，时间元组，字符串）
2.格式转换

"""
import time

"""
常见的函数

"""
# 返回自纪元(时间基准1970年1月1日)以来的当前时间的时间戳，以秒为单位,可以通过时间戳来做日期的运算
# t = time.time()
# print(t)

# 设置休眠时间
# time.sleep(1)

# 时间元组
# t = time.struct_time
# print(t)
# print(t.tm_year)

# localtime() 表示当前本地时间，返回类型为 struct_time 对象
# t = time.localtime()
# print(t)
# print(t.tm_year)
# print(t[0])

# asctime(tuple) 将时间元组转换成字符串，如果时间元组不存在，则使用localtime()返回的当前时间。
# print(time.asctime((2019, 1, 1, 9, 23, 30, 1, 1, 0)))
# print(time.asctime())

# ctime(second) 将时间戳转换成字符串，如果时间戳不存在，则使用localtime()返回的当前时间
# print(time.ctime(2))
# print(time.ctime())

# strftime() 格式化时间，将时间元组转换成字符串
# t = time.localtime()
# print(t)
# print(time.strftime("%Y-%m-%d %a %H:%M:%S", t))


"""
时间格式转换操作

"""
# # 时间戳转换成时间元组
# t = time.time() # 拿到时间戳
# print(t)
# print(time.localtime(t))    # 本地时间，北京时间
# print(time.gmtime(t))    # UTC 格林尼治标准时间，世界统一时间
# # 时间戳转换成时间字符串
# print(time.ctime(t))


# # 时间元组转换成时间戳
# t = time.localtime() # 拿到时间元组
# print(t)
# print(time.mktime(t))
# # 时间元组转换成时间字符串
# print(time.strftime('%Y-%m-%d %H:%M:%S', t))
# print(time.asctime(t))


# # 时间字符串转换成时间元组
# t = time.ctime()    # 拿到时间字符串
# print(t,type(t))
# print(time.strptime(t))
# # 时间字符串转换成时间戳
# # 没有直接的方法，可以先转换成时间元组在转换成时间戳
# print(time.mktime(time.strptime(t)))

