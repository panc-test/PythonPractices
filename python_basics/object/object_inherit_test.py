"""
继承
语法格式：
class 子类（父类）:
    pass

继承父类的构造方法：
    1.经典类的写法： 父类名称.__init__(self,参数1，参数2，...)
    2.新式类的写法：super(子类，self).__init__(参数1，参数2，....)

"""
# 定义一个父类 Person
class Person:

  def __init__(self,name,sex,age):
      self.name = name
      self.sex = sex
      self.age = age

  def get_info(self):
    print("姓名：{}\n性别：{}\n年龄：{}".format(self.name,self.sex,self.age))


# 定义一个子类Student，继承父类 Person
class Student(Person):

    def __init__(self,name,sex,age,role):   # 先继承，在重构
        Person.__init__(self,name,sex,age)  # 继承父类的构造方法
        self.role = role    # 添加参数，重构子类的构造方法

    def get_info(self): #重构父类的方法
        print("姓名：{}\n性别：{}\n年龄：{}\n角色：{}\n".format(self.name,self.sex,self.age,self.role))

    def get_role(self): #新增子类的方法
        print("角色：",self.role)


# 定义一个子类Teacher，继承父类Person，多态
class Teacher(Person):
    def __init__(self,name,sex,age,role,title):
        super(Teacher, self).__init__(name,sex,age)
        self.role = role
        self.title = title

    def get_info(self):
        print("姓名：{}\n性别：{}\n年龄：{}\n角色：{}\n职称：{}".format(self.name,self.sex,self.age,self.role,self.title))


student = Student('pan','male',18,'学生')
teacher = Teacher('li','male','38','老师','教授')
student.get_info()
teacher.get_info()