"""
一切皆对象，在内存中分配地址
类具有属性和方法

"""
class Person():
    """
    定义一个类对象Person
    """
    name = '小明'   # 类属性

    def __init__(self): # 构造方法，完成实例的初始化
        self.sex = 'male'  # 实例属性
        pass

    def eat(self):  # 实例方法，参数self
        self.age = '20' # 实例属性
        # return "this is eat method"

    @classmethod    # 类方法，参数cls
    def say(cls):
        return "this is say method"

    @staticmethod   # 静态方法，没有参数self,cls
    def run():
        return "this is run method"


print(id(Person))       #类对象
print(id(Person()))     #类的实例化对象
print(id(Person.name))  #类属性对象
print(id(Person.say()))     #类方法对象
print(id(Person().eat()))   #实例方法对象
print(id(Person().sex))     #实例属性对象






# #访问实例方法 实例对象.方法()
# print(Person().eat())
#
# #访问类方法
# print(Person.say())
# print(Person().say())
#
# #访问静态方法
# print(Person.run())
# print(Person().run())
#
# #访问类属性
# print(Person.name)
#
# #访问实例属性
# person = Person()
# print(person.sex)
# person.eat()
# print(person.age)
