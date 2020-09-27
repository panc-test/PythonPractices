"""
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

my_list.send(8)  # send()可以传递yield表达式的值进去，val=8
print(my_list.__next__())

