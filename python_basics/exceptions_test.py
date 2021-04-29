"""
异常处理机制：
1.捕获异常
2.处理机制

"""
"""
异常处理模块  
try...except...

"""
# try:
#     a = 1/0
#
# except ZeroDivisionError as e:
#     # 捕获到异常的时候执行此代码块
#     print('捕获到异常啦！')
#     print(e)
#
# except:
#     print('未知错误')



"""
异常处理模块
try...except...else...
1.只有当try 块不发生异常，才会执行 else 语句的代码块

"""
# try:
#     assert 1 == 1
#
# except (AssertionError,ZeroDivisionError) :
#     # 捕获到异常的时候执行此代码块
#     print('捕获到异常啦！')
#
# except:
#     print('未知错误')
#
# else:
#     # 没有捕获异常的时候执行此代码块
#     print("程序正常运行")



"""
异常处理模块-资源回收
try...except...finally...
1.无论 try 块是否发生异常，都会执行 finally 语句的代码块

"""
# try:
#     assert 1 == 2
#
# except (AssertionError,ZeroDivisionError) :
#     print('捕获到异常啦！')
#
# except:
#     print('未知错误')
#
# finally:
#     print("程序继续运行")



"""
显示抛出异常
raise exceptName(reason)

"""
# try:
#     a = input("输入一个数：")
#     #判断用户输入的是否为数字
#     if(not a.isdigit()):
#         raise ValueError("a 必须是数字")
#
# except ValueError as e:
#     print("发生异常：",repr(e))




"""
打印异常信息
args：返回异常的错误编号和描述字符串；
str(e)：返回异常信息，但不包括异常信息的类型；
repr(e)：返回较全的异常信息，包括异常信息的类型。

"""
# try:
#     a = 1/0
#
# except (AssertionError,ZeroDivisionError) as e:
#     print("异常信息")
#     print(e)
#     print(e.args)
#     print(str(e))
#     print(repr(e))
#
# except:
#     print('未知错误')

"""
使用 sys 模块中的 exc_info 方法打印异常信息
exc_info() 方法会将当前的异常信息以元组的形式返回，该元组中包含 3 个元素，分别为 type、value 和 traceback，它们的含义分别是：
type：异常类型的名称。
value：捕获到的异常实例。
traceback：是一个 traceback 对象。

"""
# import sys
#
# try:
#     a = 1/0
#
# except ZeroDivisionError:
#     print("异常信息")
#     print(sys.exc_info())
#
# except:
#     print('未知错误')


"""
使用 traceback 模块打印异常信息

"""
# import traceback
#
# try:
#     a = 1/0
#
# except ZeroDivisionError:
#     print("异常信息")
#     traceback.print_exc()
#
# except:
#     print('未知错误')



"""
自定义异常，继承 Exception 类，重写父类的__init__方法


"""
# # 自定义异常类 MyException
# class MyException(Exception):  # 继承异常类
#
#     def __init__(self,code,msg): # 重写父类的__init__方法
#         self.code = code
#         self.msg = msg
#
# # 捕获自定义异常类并打印输出异常信息
# try:
#     raise MyException('404','请求失败')
#
# except MyException as e:
#     print(e)

