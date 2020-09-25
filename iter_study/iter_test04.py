"""
生成器:具有yield关键字的函数都是生成器
for循环值操作yeild 生成的值

"""

def fun():
    print("start")
    yield "Jack"
    print("continue")
    yield  "Pank"
    print("end")


for i in fun():
    print("hello",i)

