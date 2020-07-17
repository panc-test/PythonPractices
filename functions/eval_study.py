'''
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
表达式：eval(expression[, globals[, locals]])
'''

print(eval('3'))
print(eval('2+4'))

#global variable
a=100
b=eval('x+1',{'x':a})
print(b)

