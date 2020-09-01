'''
内置函数：
len()：获取 列表\字符串\元组\字典 中的元素总数量（数据的长度）
max():获取数据中元素的最大值
min():获取数据中元素的最小值
sum()：对元素进行求和
eval()：识别字符串中的python表达式
zip(): 聚合打包

eval() 函数用来执行一个字符串表达式，并返回表达式的值。
表达式：eval(expression[, globals[, locals]])
'''

print(eval('3'))
print(eval('2+4'))

#global variable
a=100
b=eval('x+1',{'x':a})
print(b)

