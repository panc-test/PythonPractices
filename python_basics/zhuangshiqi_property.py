"""
特性装饰器：@property　可以把一个实例方法变成其同名属性，以支持实例访问，它返回的是一个property属性

"""

import math
class Circle():
    def __init__(self,radius): #构造器函数，圆的半径radius
        self.radius=radius

    @property
    def area(self):
        return math.pi * self.radius**2 #计算面积

    @property
    def perimeter(self):
        return math.pi*2*self.radius #计算周长


# 我们可以通过实例访问到类中属性
circle=Circle(10)
print(circle.radius)

# 通过@property装饰后的方法也可以像访问数据属性一样去访问area,会触发一个函数的执行,动态计算出一个值；
print(circle.area)
print(circle.perimeter)