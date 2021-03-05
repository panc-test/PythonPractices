"""
copy 浅拷贝
deepcopy 深拷贝

"""
import copy

"""不可变对象，元素不可变"""
# tu = (1,2,3,4,5)
# tu1 = copy.copy(tu)
# tu2 = copy.deepcopy(tu)
#
# print("对象值：",tu,tu1,tu2)
# print("对象地址：",id(tu),id(tu1),id(tu2))
# print("元素地址：",id(tu[0]),id(tu1[0]),id(tu1[0]))



"""不可变对象，元素可变"""
# tu = (1,2,3,4,[1,2])
# tu1 = copy.copy(tu)
# tu2 = copy.deepcopy(tu)
#
# print("对象值：",tu,tu1,tu2)
# print("对象地址：",id(tu),id(tu1),id(tu2))     #如果元组中元素包含列表一类的可变对象，深拷贝会重新开辟内存地址
# print("元素地址：",id(tu[-1]),id(tu1[-1]),id(tu1[-1]))
# print("子元素地址：",id(tu[-1][0]),id(tu1[-1][0]),id(tu1[-1][0]))


"""可变对象"""
list0 = [1,2,3,4,5]
list1 = copy.copy(list0)
list2 = copy.deepcopy(list0)

print("对象值：",list0,list1,list2)
print("对象地址：",id(list0),id(list1),id(list2))     #浅拷贝，深拷贝都会开辟新的内存地址
print("元素地址：",id(list0[0]),id(list1[0]),id(list2[0]))