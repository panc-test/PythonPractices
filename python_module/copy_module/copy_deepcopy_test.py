"""
浅拷贝，深拷贝分析
1.浅拷贝只拷贝父对象，不拷贝子对象，深拷贝会拷贝父对象和子对象。
2.拷贝不可变对象内存地址不变，拷贝可变对象会开辟新的内存地址。

"""
import copy

# # 不可变对象，元素不可变
# # obj = 100
# # obj = 'abcd'
# obj = (1,2,3,4,5)
# obj1 = copy.copy(obj)
# obj2 = copy.deepcopy(obj)
#
# print("对象值：",obj,obj1,obj2)
# print("对象地址：",id(obj),id(obj1),id(obj2))
# print("元素地址：",id(obj[0]),id(obj1[0]),id(obj2[0]))



# # 不可变对象，元素可变
# obj = (1,2,3,4,[1,2])
# obj1 = copy.copy(obj)
# obj2 = copy.deepcopy(obj)
#
# print("对象值：",obj,obj1,obj2)
# print("对象地址：",id(obj),id(obj1),id(obj2))     #如果元组中元素包含列表一类的可变对象，深拷贝会重新开辟内存地址
# print("元素地址：",id(obj[-1]),id(obj1[-1]),id(obj2[-1]))
# print("子元素地址：",id(obj[-1][0]),id(obj1[-1][0]),id(obj2[-1][0]))


# # 可变对象，元素不可变
# obj = [1,2,3,4,5]
# obj1 = copy.copy(obj)
# obj2 = copy.deepcopy(obj)
#
# print("对象值：",obj,obj1,obj2)
# print("对象地址：",id(obj),id(obj1),id(obj2))     #浅拷贝，深拷贝都会开辟新的内存地址
# print("元素地址：",id(obj[0]),id(obj1[0]),id(obj2[0]))


# 可变对象，元素可变
obj = [1,2,3,4,[1,2]]
obj1 = copy.copy(obj)
obj2 = copy.deepcopy(obj)

print("对象值：",obj,obj1,obj2)
print("对象地址：",id(obj),id(obj1),id(obj2))     #浅拷贝，深拷贝都会开辟新的内存地址
print("元素地址：",id(obj[-1]),id(obj1[-1]),id(obj2[-1]))
print("子元素地址：",id(obj[-1][0]),id(obj1[-1][0]),id(obj2[-1][0]))