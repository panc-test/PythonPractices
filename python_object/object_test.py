"""
一切皆对象

"""
class Person():
    """
    定义一个类对象Person
    """
    grade = '一班'   # 类属性

    def __init__(self,name,sex,age): # 构造方法，完成实例的初始化
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self,weight):  # 实例方法，参数self
        self.weight = weight # 实例属性
        print("this is eat method")

    @classmethod    # 类方法，参数cls
    def say(cls):
        print("this is say method")

    @staticmethod   # 静态方法，没有参数self,cls
    def run():
        print("this is run method")


print("访问实例化方法：")
Person('pan','male',18).eat('60kg')

print("访问类方法：")
Person.say()
Person('pan','male',18).say()

print("访问静态方法：")
Person.run()
Person('pan','male',18).run()

print("类属性：")
print(Person.grade)

print("实例属性：")
student = Person('pan','male',18)
student.eat('60kg')   # 注意只有先调用了实例方法，才能拥有实例属性
print(student.weight)
