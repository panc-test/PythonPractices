"""
去除列表中的重复数据

"""

lst = ['b','c', 'd','b','c','a','a']

#方法1：使用内置函数 set(), sorted 函数对所有可迭代的对象进行排序操作,key=list.index 可以保持原列表的顺序。
list1 = set(lst)
print("list1 = ",list1)
print("list1 = ",sorted(list1,key=lst.index))

#方法2：字典的{}.fromkeys()方法
list2 = {}.fromkeys(lst).keys()
print("list2 = ",list(list2))

#方法3：遍历去除重复
list3 = []
for r in lst:
    if r not in list3:
        list3.append(r)
print("list3 = ",list3)

#方法4：列表推导式
list4 = []
[list4.append(i) for i in lst if i not in list4]
print("list4 = ",list4)
