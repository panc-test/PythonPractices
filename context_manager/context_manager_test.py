"""
上下文管理器
1.__enter__() 从该方法进入运行时上下文，返回当前对象或者与运行时上下文相关的其他对象。
如果with语句有as关键词存在，返回值会绑定在as后的变量上。

2.__exit__(exc_type, exc_val, exc_tb) 退出运行时上下文，返回一个布尔值标示是否有需要处理的异常。
如果在执行with语句体时发生异常，那退出时参数会包括异常类型、异常值、异常追踪信息，否则，3个参数都是None。

"""


# !/usr/bin/env python
# coding=utf-8

# # 自定义上下文管理器
# class MyContextManager:
#
#     def __enter__(self):
#         print("Starting the Manager.")
#
#     def __exit__(self, *others):
#         print("Exiting the Manager.")
#
#
# with MyContextManager():
#     print("In the Manager.")


class MyContextManagerOpenDemo:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('Starting the Manager')
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting the Manager')
        self.open_file.close()


with MyContextManagerOpenDemo('mytest.txt', 'r') as reader:
    print('In the Manager')
    print(reader.readlines())
