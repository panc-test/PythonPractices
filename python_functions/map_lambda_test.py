"""
1.map() 函数根据提供的函数对指定序列做映射。  -----关联记忆 filter 函数映射
语法格式：map(function, iterable)
说明：iterable 中的元素逐个调用 function 函数，返回一个迭代器。

2.lambda 匿名函数
语法格式 : lambda arguments : expression

"""
#计算幂函数
# lst = [1, 2, 3, 4]
# map_list = map(lambda x : x **2,lst)
# print(map_list)
# new_list = list(map_list)
# print(new_list)


#首字母大写,其它小写
name_list={'tony','cHarLIE','rachAEl'}
def format_name(s):
    ss=s[0:1].upper()+s[1:].lower()
    return ss
new_list = list(map(format_name,name_list))
print (new_list)
