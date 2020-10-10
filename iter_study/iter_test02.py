"""
可迭代的对象 :只有__iter__方法,没有__next__方法。

"""
#自定义一个可迭代的对象
class Iter1:
  def __init__(self, text):
    self.text = text

  def __iter__(self):
    return iter(self.text)

#实例化一个可迭代对象
iter1 = Iter1("hello")
print(type(iter1))

#for 循环遍历迭代器
for s in iter1:
  print(s)

