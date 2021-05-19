'''
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
exec() 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。

'''
print(eval('2+4'))
exec('print("hello world")')

# #global variable
# a = 100
# b = 200
# new_a = eval('x+1',{'x':a})
# new_b = eval('x+1',{'x':b})
# print(new_a)
# print(new_b)


f = open('./test_datas/test_exec.txt','r')
s = f.read()
exec(s)




