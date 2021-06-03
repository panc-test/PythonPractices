"""
1.sorted()  默认升序，返回一个新列表
2.reversed() 反转序列，返回一个迭代器对象，只单纯的反转元素，不去重，不排序

注意：
sort()是列表的内置方法，只作用于列表，默认升序，直接修改原有的列表元素顺序，返回NONE。

"""
list1 = [2,5,4,3,1]
list2 = [2,3,1,8,0]
list3 = [3,4,1,2,8]

# sorted
print(sorted(list1))
print(list1)

# sort
print(list2.sort())
print(list2)

# reversed
print(reversed(list3))
print(list3)
list31 = []
for i in reversed(list3):
    list31.append(i)
print(list31)



