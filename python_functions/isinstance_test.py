"""
isinstance() 函数来判断一个对象是否是一个已知的类型，返回值是True or False
语法格式：isinstance(object, tuple)
参数：
object -- 实例对象。
tuple -- 基本类型或者由它们组成的元组，也可以是直接或间接类名。

"""
print(isinstance('hello', (int, str)))  #注意不是 string


# 父类
class Parent(object):
    pass

#子类
class Sub(Parent):
    pass

#实例化
A = Parent()
B = Sub()

# isinstance() 会认为子类是一种父类类型，考虑继承关系。
print(isinstance(Sub, Parent))
print(isinstance(A, Parent))
print(isinstance(A, Sub))
print(isinstance(B, Parent))
print(isinstance(B, Sub))