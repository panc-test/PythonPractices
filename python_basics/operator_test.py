"""
运算符操作
1.数学运算
2.逻辑运算
3.赋值运算
4.位运算符
https://www.runoob.com/python3/python3-basic-operators.html#ysf1

"""
# # 数学运算符
# a = 10
# b = 3
# print(a / b)
# print(a // b) # 取整
# print(a % b)  # 取余数
# print(a ** b)   # 幂运算



# # 赋值运算
# a = 10
# a +=1   # 等同于 a = a + 1
# print(a)
# a -=1   # 等同于 a = a - 1
# print(a)




# 逻辑运算
str = 'aaaaaaaaaavvvvvvvvvvvvvvv'
print('a' in str)
print('b' not in str)

a = [1,2,3]
b = [1,2,3]
print(id(a))    # 列表是可变数据类型，内存地址不同，int，string，tuple是不可变数据类型，内存地址相同
print(id(b))
print(a == b)   # 判断2个变量值是否相等
print(a is b)   # 判断2个变量是否引用同一内存地址
print(a is not b)