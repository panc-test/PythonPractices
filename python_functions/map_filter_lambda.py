"""
1.map() 函数根据提供的函数对指定序列做映射,序列中的元素逐个调用函数，返回值是一个map对象
语法格式：map(function, iterable)

2.filter() 函数用来过滤序列，使用函数过滤序列中不符合条件的元素，返回值是一个filter对象
语法：filter(function, iterable)

3.lambda 匿名函数，接受任意多个参数，返回值是一个function对象
语法格式 : lambda arguments : expression

"""
# map函数首字母大写,其它小写
name_list=['tony','cHarLIE','rachAEl']

def format_name(s):
    ss=s[0].upper()+s[1:].lower()
    return ss

print(map(format_name,name_list))
print (list(map(format_name,name_list)))


# filter函数过滤列表中的所有奇数
lst = [0,1,2,3,4,5,6,7,8,9]
def func(n):
    return n%2

print(filter(func, lst))
print(list(filter(func, lst)))



# lambda匿名函数结合map函数做幂运算
lst = [1, 2, 3, 4]
function = lambda x: x ** 2
print(function)
print(list(map(function, lst)))



# lambda匿名函数结合filter函数使用
print(list(filter(lambda x: x%2, range(10))))