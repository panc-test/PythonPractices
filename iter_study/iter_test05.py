"""
生成器：
yield可以理解为return，返回后面的值给调用者。
不同的是return返回后，函数会释放，而生成器则不会。
在直接调用next方法或用for语句进行下一次迭代时，生成器会从yield下一句开始执行，直至遇到下一个yield。
"""
def myList(num):  # 定义生成器

    now = 0  # 当前迭代值，初始为0
    while now < num:
        val = (yield now)  # 返回当前迭代值，并接受可能的send发送值；yield在下面会解释
        if val is None: # val为None，迭代值自增1，否则重新设定当前迭代值为val
            now = now + 1
        else: val


my_list = myList(5)  # 得到一个生成器对象
print(my_list.__next__())
print(my_list.__next__())

my_list.send(1)  # 重新设定当前的迭代值
print(my_list.__next__())
print(my_list.__next__())
