"""
python 闭包
定义：
一个函数中定义了另一个函数，并且内部函数引用了外部函数的参数和局部变量，外部函数返回值是内部函数。
特点：
1.内部函数引用了外部函数的参数和局部变量，这些参数可能是外部函数的自己定义的变量，也可能是外部函数被调用传入的参数
2.内部函数不能直接修改外部函数的参数和局部变量，这个时候可以使用关键字 nonlocal
3.外部函数返回值是内部函数

"""
def outer(x):   # 外部函数
    a = 1   # 外部函数局部变量
    def inner(y):   #内部函数
        nonlocal x
        x = x+a
        print(x)
        return x+y
    return inner    #外函数返回值是内函数

closure = outer(1)
print(closure(3))


# #使用闭包计算一个数的 n 次幂
# def math_power(power):
#
#     def math_base(base):
#         return base ** power
#
#     return math_base
#
# square = math_power(2) # 计算一个数的平方
# cube = math_power(3) # 计算一个数的立方
#
# print(square(2))  # 计算 2 的平方
# print(cube(2)) # 计算 2 的立方