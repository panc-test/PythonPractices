"""
with - 上下文管理器

"""

with open('mytest.txt', 'r') as f:
    """
    对象f具有__enter__和__quit__方法
    """
    # print(dir(f))
    print(f.__enter__())
    print(f.__exit__())