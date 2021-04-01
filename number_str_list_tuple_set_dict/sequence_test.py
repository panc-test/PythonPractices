"""
序列类型 —— 字符串、列表、元组、集合和字典
1.索引切片
2.序列相加
3.序列相乘
4.其它
注意：
集合和字典不支持索引、切片、相加和相乘操作。

"""

str = "Python"
list = [1,2,3,4,5]
tuple = ('one','two','three')

#索引切片
print(str[1:3])
print(list[1:])
print(tuple[:],"\n")

#序列相加
print(str+'123')
print(list+[1,2])
print(tuple+(1,2),'\n')

#序列相乘
print(str*2)
print(list*2)
print(tuple*2,'\n')

#检查元素是否在序列中
print('p' in str)
print('p' not in str)