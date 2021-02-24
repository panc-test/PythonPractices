"""
数据格式转换函数大全:
"""

"""
int() 函数将一个字符串或数字转换为整型,向下取整
语法格式 ： int(x, base=10)
 x -- 字符串或数字
 base -- 进制数，默认十进制
"""
# print(int("123"))
# print(int(12.857))


"""
float() 函数用于将整数和字符串转换成浮点数。
语法格式 ： float(x)
"""
# print(float(10.00))
# print(float("10"))


"""
str() 函数返回一个对象的string格式。
repr() 函数返回一个对象的string格式.
str() 的输出追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
repr() 的输出追求明确性，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用。
"""
# a = 123
# print(type(str(a)),str(a))
# print(type(repr(a)),repr(a))


"""
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
语法格式 ： eval(expression,globals,locals)
expression -- 表达式。
globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
"""
# print(eval("1+1"))


"""
chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。返回值是当前整数对应的 ASCII 字符。
语法格式 ： chr(i)
i -- 可以是10进制也可以是16进制的形式的数字。
ASCII 字符码：http://c.biancheng.net/c/ascii/

ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
"""
print(chr(48))
print(ord("0"))


"""
complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
语法格式 ： complex(real,imag)
real -- int, long, float或字符串；
imag -- int, long, float；
"""
# print(complex(1, 2))
