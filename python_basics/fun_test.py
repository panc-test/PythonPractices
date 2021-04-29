"""
fun指的是函数本身
fun()指的是函数的返回值

"""
def fun():
    return 1

print(fun)
print(fun())



def outer(x):   # 外部函数

    def inner(y):   #内部函数
        return x+y

    return inner    #外函数返回值是内函数
