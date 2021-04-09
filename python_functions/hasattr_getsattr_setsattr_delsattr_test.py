"""
hasattr(object, attribute)    判断对象中是否包含指定的属性,如果对象有该属性返回 True，否则返回 False。
setattr(object, attribute,default)  获取对象中指定属性的值,获取失败的话报 AttributeError 异常，或者指定报错信息。
getattr(object, attribute,value)  修改对象中指定属性的值，若属性不存在，先创建再赋值。
delattr(object, attribute)  删除对象中中指定的属性

"""
class Person:
  name = "xiaoming"
  sex = "man"
  age = 20

#实例化
p = Person()

#判断
# print(hasattr(p, 'age'))

#取值
# print(getattr(p, 'age', '没有属性age'))
# print(getattr(p, 'country', '没有属性country'))

#修改
# setattr(p,'age','21')
# print(p.age)

#创建
# setattr(p,'country','China')
# print(hasattr(p, 'country'))
# print(getattr(p, 'country'))

#删除
delattr(Person,'age')   # 注意这里不能用 p
print(hasattr(p, 'age'))
