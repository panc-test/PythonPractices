"""
问题：列表 [1,  2, 3, 8, 9]，要求你把列表里面的每个值加1


"""


list0 = [1,  2, 3, 8, 9]
list_new = [i+1 for i in list0]  #列表推导式
print(list_new)