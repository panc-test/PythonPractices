"""
分析异常传播轨迹

"""
import traceback

def fun1():
    fun2()

def fun2():
    fun3()

def fun3():
    raise Exception("抛出异常，可以自定义异常")

fun1()
#
# try:
#     fun1()
# except:
#     # 控制台打印输出异常信息
#     traceback.print_exc(limit=1)
#     # 将异常信息写入到指定文件中
#     traceback.print_exc(file=open("exception_log.txt","a"))