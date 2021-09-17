"""
数据类型转换函数：
int()   转换成整数，参数可以是 number，string
float() 转换成浮点数，对象可以是int,string
complex()   转换成复数，参数可以是 int，float，string

"""
# int()
# 不带参数 base
print(int())    # 空值
print(int(True))    # bool类型
print(int(False))
list = [1,1.2,1.5,1.8,-8.2] # int和float类型
for i in list:
    print(int(i))
print(int('11'))    # 字符串类型

# 带参数 base
print(int('11',2))  # 2进制转换成10进制
print(int('11', 8)) # 8进制转换成10进制
print(int('11',16)) # 16进制转换成10进制



# float()
print(float(1))
print(float('1'))



# complex()
# 一个参数
print(complex(1))
print(complex(1.5))
print(complex('2'))

# 多个参数
print(complex(1, 2))
