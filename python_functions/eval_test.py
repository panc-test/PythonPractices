'''
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
表达式：eval(expression,globals,locals)
expression -- 表达式。
globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

'''

print(eval('3'))
print(eval('2+4'))

#global variable
a=100
b=eval('x+1',{'x':a})
print(b)
