"""
generator.send(value)
恢复执行并向生成器函数“发送”一个值。 value 参数将成为当前 yield 表达式的结果。
send() 方法会返回生成器所产生的下一个值，或者如果生成器没有产生下一个值就退出则会引发 StopIteration。
当调用 send() 来启动生成器时，它必须以 None 作为调用参数，因为这时没有可以接收值的 yield 表达式。

1、__next__()方法不能传递特定的值，只能传递None给yield表达式
2、send()方法可以传递给yield表达式值，

"""

def myList(num):  # 定义生成器

    now = 0
    while now < num:
        val = yield now
        if val is None:     #val 为什么一直是 None
            now = now + 1
        else:
            print("xxxxxxxx")


my_list = myList(5)
print(my_list.__next__())   #__next__()不能传递特定的值，只能传递None进去,所以if语句一直成立
print(my_list.__next__())
my_list.send(8)  # send()可以传递yield表达式的值进去，将8传递给val，这个时候val= 8
print(my_list.__next__())

