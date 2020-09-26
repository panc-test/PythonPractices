"""
迭代器：
1、如果在一个类中定义__iter__方法，那么这个类的实例就是一个迭代器。
2、__iter__方法需要返回一个迭代器，所以就返回对象本身即可(也就是self)。
3、当对象每迭代一次时，就会调用迭代器中的另外一个特殊成员方法__next__。该方法需要返回当前迭代的结果，超出边界值会抛出StopIteration异常。

"""
#自定义可迭代的类
class MyIter:

  def __init__(self, start, end):
    self.count = start
    self.end = end

  def __iter__(self):
    return self

  def __next__(self):
    if self.count < self.end:
      result = self.count
      self.count += 1
      return result
    else:
      raise StopIteration

#实例化一个迭代器
it = MyIter(1, 10)
print('对象it的类型：',type(it))

#for 循环遍历迭代器
for i in it:
  print(i)








