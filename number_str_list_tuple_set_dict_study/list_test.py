"""
python基础数据类型 ——列表 list(可变，有序的，可重复的)
增：append,extend,insert
删: del,pop,remove,clear
改：直接赋值
查：切片,count,index


"""

"""
创建列表

"""
# list1 = [1,2,2,5,3,4]
# list2 = list("hello")
# list3 = list(range(5))
# print(list1)
# print(list2)
# print(list3)

"""
访问列表中的元素——切片  
语法：list[start:stop:step]
*****注意左开右闭

"""
# list = [0,1,2,3,4,5,6,7,8,9]
# print(list[0])
# print(list[-1])
# print(list[1:5])
# print(list[1:])
# print(list[:])
# print(list[::2])   #步长为2
# print(list[::-1]) # 步长为-1，反转列表


"""
更新列表元素

"""
# list = [1,2,2,5,3,4]
# list[0] = "a"
# print(list)


"""
删除列表元素

"""
# list1 = [1,2,3,4,5]
# list2 = [1,2,3,4,5,6,7,8,9]
# del list1[0]
# del list2[1:5]
# print(list1)
# print(list2)



"""
拼接列表

"""
# list1 = [1,2]
# list2 = [3,4]
# print(list1+list2)


"""
嵌套列表

"""
# list1 = [1,2]
# # list2 = [3,4]
# # list3 = [list1,list2]
# # print(list3)


"""
列表方法
'append', 'extend', 'insert',
'pop', 'remove', 'clear',
'count', 'index', 
'sort','copy', 'reverse', 

"""

"""
 append() 方法用于在列表末尾添加新的对象。该方法无返回值。
 格式 ： list.append(obj)
 
"""
# list = [1,2,3,2]
# list.append(5)
# print(list)


"""
 extend() 方法用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。该方法没有返回值。
 格式 ： list.extend(seq)
  
 """
# list = [1,2,2]
# list.extend([3,3,5])
# list.extend(range(5))
# print(list)



"""
insert() 方法用于将指定对象插入列表的指定位置。该方法没有返回值。
格式 ： list.insert(index, obj)
index -- 对象obj需要插入的索引位置。
obj -- 要插入列表中的对象。

"""
# list = [1,2,3]
# # list.insert(1,"obj")
# # print(list)



"""
pop() 方法用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
格式 ： list.pop(index)
index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。

"""
# list =[1,2,3,4,5]
# a = list.pop(2)
# print(a)
# print(list)


"""
remove() 方法只会删除列表中第一个和指定值相同的元素，而且必须保证该元素是存在的，否则会引发 ValueError 错误
格式 ： list.remove(obj)
obj -- 列表中要移除的对象。

"""
# list = [1,4,2,3,4]
# list.remove(4)
# print(list)



"""
clear() 方法用于清空列表，类似于 del a[:]。
格式 ： list.clear()

"""
# list = [1,3,4,5]
# list.clear()
# print(list)



"""
count() 方法用于统计某个元素在列表中出现的次数。
格式 ： list.count(obj)

"""
# list = ["a","A",2,3,4]
# print(list.count("a"))    #区分大小写


"""
index() 方法用来查找某个元素在列表中出现的位置（也就是索引），如果该元素不存在，则会导致 ValueError 错误
格式 ： list.index(obj, start, end)
obj-- 查找的对象。
start-- 可选，查找的起始位置。
end-- 可选，查找的结束位置。

"""
# list = [1,2,3,4,2,5]
# print(list.index(2))
# print(list.index(2,3))



"""
reverse() 方法用于反向列表中元素。
格式 ： list.reverse()

"""
# list = [1,2,3,4]
# list.reverse()
# print(list)


"""
sort() 方法用于对原列表进行排序(默认升序)，如果指定参数，则使用比较函数指定的比较函数。
格式 ： list.sort( key=None, reverse=False)
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。

"""
# list = [2,3,1,5,4]
# list.sort()
# print(list)


"""
copy() 方法用于复制列表，类似于 a[:]。返回复制后的新列表。
格式 ： list.copy()

"""
# list1 = [1,2,3,4]
# list2 = list1.copy()
# print(list2)