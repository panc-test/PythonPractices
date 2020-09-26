"""
生成器：
yield可以理解为return，返回后面的值给调用者。
不同的是return返回后，函数会释放，而生成器则不会。
在直接调用next方法或用for语句进行下一次迭代时，生成器会从yield下一句开始执行，直至遇到下一个yield。
"""
def myList(num):  # 定义生成器

    now = 0  # 当前迭代值，初始为0
    while now < num:
        val = yield now  # 这里的yield返回当前迭代值，相当于return
        if val is None:     #val 为什么一直是 None
            now = now + 1
        else:
            print("xxxxxxxx")


my_list = myList(5)
print(my_list.__next__())   #__next__()不能传递特定的值，只能传递None进去,所以if语句一直成立
print(my_list.__next__())

my_list.send(8)  # send()可以传递yield表达式的值进去
print(my_list.__next__())

