"""
生成器:
一种特殊的迭代器，使用yield返回结果。yield语句执行后，挂起函数的状态，以便下次从它离开的地方继续执行。
生成器常用方法：
1.__next__()方法，返回yield关键字后面表达式的值。
2.send()方法，接受外部传入的一个参数，该参数指定的是上一次被挂起的yield语句的返回值。send()可以传递yield表达式的值进去。
3.throw()方法，抛出异常
4.close()方法，

"""
# # next方法
# def myGenerator():
#     yield "start"
#     yield "expression"
#     yield "end"
#
# gen = myGenerator()
# print(gen)
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# # print(gen.__next__())



# next方法不能传递特定的值，只能传递None进去
def myGenerator():
    value = yield "start"
    yield value
    yield "end"

gen = myGenerator()
print(gen)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())



# # send方法
# def myGenerator():
#     value1 = yield "start"
#     yield value1
#     yield "end"
#
# gen = myGenerator()
# print(gen)
# print(gen.__next__())
# print(gen.send("expression"))
# print(gen.__next__())








# # 定义生成器
# def myGenerator(num):
#
#     now = 0
#     while now < num:
#         val = yield now
#         if val is None:
#             now = now + 1
#         else:
#             print("StopIteration")
#
#
# my_generator = myGenerator(5)
# print(my_generator.__next__())  # __next__()不能传递特定的值，只能传递None进去,所以if语句一直成立
# print(my_generator.__next__())
# my_generator.send(8)  # send()方法,该参数指定的是上一次被挂起的yield语句的返回值。
# print(my_generator.__next__())
