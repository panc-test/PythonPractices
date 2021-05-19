"""
hasattr(object, attribute)    判断对象中是否包含指定的属性,如果对象有该属性返回 True，否则返回 False。
getattr(object, attribute,value)  获取对象中指定属性的值,获取失败的话报 AttributeError 异常，或者指定报错信息。
setattr(object, attribute,default)  修改对象中指定属性的值，若属性不存在，先创建再赋值。
delattr(object, attribute)  删除对象中中指定的属性

"""
# 定义一个类对象
class Person:
  name = "xiaoming"
  sex = "man"
  age = 20

  def __init__(self):
    pass

#判断
print(hasattr(Person, 'age'))

#取值
print(getattr(Person, 'age'))
print(getattr(Person, 'country', '没有属性 country'))

#修改属性
setattr(Person,'age','21')
print(Person.age)

#创建属性
setattr(Person,'country','China')
print(getattr(Person, 'country', '没有属性 country'))

#删除属性
delattr(Person,'age')
print(hasattr(Person, 'age'))
