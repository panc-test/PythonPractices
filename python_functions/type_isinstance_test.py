"""
1.type(object) 函数返回对象的类型，int,float,bool,complex,str,list,tuple,set,dict
2.isinstance(object, classinfo)
    如果 classinfo 是指定的类型，则 isinstance() 函数返回 True，否则返回 False。
    如果 classinfo 参数是元组，则如果对象是元组中的类型之一，那么此函数将返回 True。

区别：
isinstance() 会认为子类是一种父类类型，考虑继承关系。
type() 不会认为子类是一种父类类型，不考虑继承关系。

"""

print(type(100))
print(isinstance('hello', (int, str)))  #注意不是 string