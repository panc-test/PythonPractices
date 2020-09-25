
#str()函数可以将数值型转换成字符型

a='小明的数学分数：'
b=88
c=a+str(b)      #使用'+'拼接字符串
print(c)

d=a+repr(b)     #repr() 函数也可以将数字转换成字符串
print(d)

