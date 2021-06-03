"""
迭代器：
1、如果在一个类中定义__iter__方法和__next__方法，那么这个类的实例就是一个迭代器。
2、__iter__方法需要返回一个迭代器，所以就返回对象本身即可(也就是self)。
3、当对象每迭代一次时，就会调用迭代器中的另外一个特殊成员方法__next__。该方法需要返回当前迭代的结果，超出边界值会抛出StopIteration异常。

"""


# 自定义迭代器
class MyIter:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    # 返回一个迭代器
    def __iter__(self):
        return self

    # 定义迭代规则
    def __next__(self):
        if self.start < self.end:
            self.start += 1
            return self.start
        else:
            raise StopIteration


# 实例化一个迭代器
it = MyIter(5, 10)
# for 循环遍历迭代器
for i in it:
    print(i)
