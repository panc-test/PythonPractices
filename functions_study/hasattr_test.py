"""
hasattr() 函数用于判断对象是否包含对应的属性。如果对象有该属性返回 True，否则返回 False。
语法：hasattr(object, attribute)
object -- 对象。
attribute -- 字符串，属性名。

先关函数：
setattr()
getattr()
delattr()

"""
class Person:
  name = "Bill"
  age = 63
  country = "USA"

p = Person()
print(hasattr(p, 'age'))