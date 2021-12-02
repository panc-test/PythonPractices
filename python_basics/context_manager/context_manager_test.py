"""
上下文管理器(ContextManager)；
1.__enter__() 进入上下文，返回当前对象或者与运行时上下文相关的其他对象。
一般用来处理操作前的内容。比如一些创建对象，初始化等。
如果with语句有as关键词存在，返回值会绑定在as后的变量上。

2.__exit__(exc_type, exc_val, exc_tb) 退出上下文，返回一个布尔值标示是否有需要处理的异常。
一般用来处理一些善后收尾工作，比如文件的关闭，数据库的关闭等。
如果在执行with语句体时发生异常，那退出时参数会包括异常类型、异常值、异常追踪信息，否则，3个参数都是None。
return返回值决定了捕获的异常是否继续向外抛出，没有return 就默认为 return False。
如果是 False 那么就会继续向外抛出，程序会看到系统提示的异常信息
如果是 True 不会向外抛出，程序看不到系统提示信息，只能看到打印的输出

"""


# # 自定义上下文管理器
# class MyContextManager:
#
#     def __enter__(self):
#         print("-- Starting the Manager --")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("-- Exiting the Manager --")
#
#
# with MyContextManager():
#     print("-- In the Manager --")


# # 自定义带参数的上下文管理器
# class MyContextManagerOpenDemo:
#
#     def __init__(self, filename, mode):
#         """
#         实例化对象的时候必须带上的参数
#         """
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         """
#         进入上下文管理器，打开指定文件，返回文件对象
#         """
#         print('--- Starting the Manager ---')
#         self.open_file = open(self.filename, self.mode)
#         return self.open_file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """
#         退出上下文管理器，关闭文件对象。
#         """
#         print('--- Exiting the Manager ---')
#         self.open_file.close()
#
# with MyContextManagerOpenDemo('mytest.txt', 'r') as f:
#     print('--- In the Manager ---')
#     print(f.read())


# 执行with语句时候发生异常，异常处理
class MyContextManagerOpenDemo:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('--- Starting the Manager ---')
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('--- Exiting the Manager ---')
        self.open_file.close()
        print('Type: ', exc_type)
        print('Value:', exc_val)
        print('TreacBack:', exc_tb)
        # 抛出异常
        return True


with MyContextManagerOpenDemo('mytest.txt', 'r') as f:
    print('--- In the Manager ---')
    print(f.write('sss'))
