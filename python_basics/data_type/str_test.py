"""
python基础数据类型-字符串 string(不可变数据类型)

"""
"""
创建字符串
1.单引号
2.双引号
3.双引号+单引号

"""
# a = ''
# b = '123'
# c = "abc"
# d = 'abc "123"'
# print(a)
# print(b)
# print(c)
# print(d)


"""
字符串访问：
1.索引
2.切片
3.for循环

"""
# str = 'hello world'
# #索引
# print(str[0])
# #切片
# print(str[1:4])
# #for循环
# for s in str:
#     print(s)


"""
运算符操作：
1.数学运算(字符串拼接，字符串复制)
3.逻辑运算（true,false）

"""
# a = 'hello '
# b = 'world'
# c = 'world'
# #字符串拼接
# print(a+b)
# #复制字符串
# print(a*3)
# #相等判断
# print(a == b)
# print(a != b)
# #身份运算符
# print(b is c)
# print(a is not b)
# #成员运算符
# print('h' in a)
# print('h' not in a)



"""
转义字符：\n

"""
# #换行
# print("hello\nworld")
# #不换行
# print("hello aaaaaaaaaaaaaa\
#       world")
# #单引号
# print('what\'s your name?')




"""----------------------字符串内置方法---------------------------------------------------"""
"""
正则表达式：
语法：r'正则表达式' ,r是非转义字符
功能：检查一个字符串是否与某种模式匹配。
模块：re
注意：
这里只简单的看下使用正则表达式处理字符串，关于正则表达式的用法后续会详细学习。

"""
# import re
# str = "a123b"
# print(re.findall(r"a(.+?)b", str))  # 匹配字符串a到b之间的所有字符


"""
函数操作：
len(string)：返回字符串长度
str(object)：将object转换成string类型，给人看
repr(object)：将object转换成string类型，给机器看
eval()：执行一个字符串表达式，并返回表达式的值。

"""
# a = 100
# b = str(a)
# c = repr(a)
# d = eval(c)
#
# print(b,type(b))
# print(c,type(c))
# print(d,type(d))



"""
字符串编码解码：
1.encode() 方法编码。将人类可识别的字符转换为机器可识别的字节码 / 字节序列
2.decode() 方法解码。编码的反向过程叫解码

"""
# info = 'hello 你好'
#
# result = info.encode(encoding='UTF-8') # 以UTF-8规则进行编码
# print(result)
#
# actual = result.decode(encoding='UTF-8')# 以UTF-8规则进行解码，得到正确结果
# print(actual)
#
# actual = result.decode(encoding='gbk') # 以gbk规则进行解码，得到错误结果
# print(actual)
#


"""
格式化字符串：
format() 方法。
格式：'{}'.format(args)

"""
# #一个参数
# print('this {} example'.format('is'))
# #多个参数，不指定位置，按默认顺序
# print('{} {}'.format('hello','world'))
# #多个参数，设置指定位置
# print('{0} {0} {1}'.format('hello','world'))
#
# #格式化数字
# print("{:.2f}".format(3.1415926))  #保留2位小数



"""
查找元素：
1.find() 方法返回指定范围内字符串第一次出现的索引，如果没有匹配项则返回-1。
2.rfind() 方法返回指定范围内字符串最后一次出现的索引，如果没有匹配项则返回-1。
3.index() 方法返回指定范围内字符串第一次出现的索引，如果没有匹配项则抛出异常。
4.rindex() 方法返回指定范围内字符串最后一次出现的索引，如果没有匹配项则抛出异常。

"""
# str = "this is string example....wow!!!"
# print(str.find('is'))
# print(str.rfind('is'))
# print(str.index('is'))
# print(str.rindex('is'))


"""
对齐方式：
1.ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
2.rjust() 方法返回一个原字符串右对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
3.center() 方法返回一个原字符串居中对齐,并使用空格填充至指定长度的新字符串。默认填充字符为空格。
    语法：str.ljust(width, fillchar)
    width -- 指定字符串长度。
    fillchar -- 填充字符，默认为空格。

"""
# str = "this is string example"
# print(str.ljust(30,'*'))
# print(str.rjust(30,'*'))
# print(str.center(30,'*'))


"""
大小写转换：
1.upper() 方法用于将字符串中的所有小写字母转换为大写字母。
2.lower() 方法用于将字符串中的所有大写字母转换为小写字母。
3.title() 方法用于将字符串中每个单词的首字母转为大写，其他字母全部转为小写。
4.capitalize() 将字符串的第一个字母变成大写,其他字母变小写。

注意：
这几张方法都不会改变原始字符串，字符串是不可变的
 
"""
# str = "hello WORLD"
# print(str.upper())
# print(str.lower())
# print(str.title())
# print(str.capitalize())


"""
删除字符：
1.strip()：删除字符串前后（左右两侧）的空格或特殊字符或字符序列。
2.lstrip()：删除字符串前面（左边）的空格或特殊字符。
3.rstrip()：删除字符串后面（右边）的空格或特殊字符。
    语法：str.strip(chars)
    chars -- 移除的字符序列
注意：
1.这里的特殊字符指的是制表符（\t）、回车符（\r）、换行符（\n）等。
2.返回移除字符串头尾指定的字符后生成的新字符串

"""
# str1 = " hello world    "
# print(str1.strip())
# print(str1.lstrip())
# print(str1.rstrip())

# str2 = "hello world\n"
# print(str2.strip())

# str3 = "1110123456789110"
# print(str3.strip('1'))  #头尾开始检索，删除等于1的字符，遇到第一个不是1的字符时候停止删除
# print(str3.strip('01')) #头尾开始检索，删除等于0或者1的字符，遇到第一个不是0和1的字符时候停止删除


"""
拼接字符串：
join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
语法：str.join(sequence)

"""
seq = ['www','runoob','com']
url = '.'.join(seq)
print(url)

"""
分割字符串：
split() 通过指定分隔符对字符串进行切片，返回分割后的字符串列表。
语法：str.split(sep,maxsplit)
sep -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
maxsplit -- 分割次数。默认为 -1, 即分隔所有。如果参数 num 有指定值，则分隔 num+1 个子字符串,

"""
# url = 'www.runoob.com'
# a=url.split(sep='.')
# print(a)

"""
统计字符串：
count() 方法用于统计字符串里某个字符出现的次数。
语法：str.count(sub, start,end)
sub -- 搜索的字符
start -- 字符串开始搜索的位置。默认为第一个字符。
end -- 字符串中结束搜索的位置。默认为字符串的最后一个位置。

"""
# str = "this is string example"
# print(str.count('s'))
# print(str.count('s',1,5))



"""
替换字符串：
replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
语法：str.replace(old,new,max)
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次

"""
# str = "this is string example....wow!!! this is really string"
# a = str.replace('this','THIS')
# print(a)
# print(str)



"""
startswith() 方法用于检索字符串是否以指定字符串开头，如果是返回 True；反之返回 False。
endswith() 方法用于检索字符串是否以指定字符串结尾，如果是则返回 True；反之则返回 False。

"""
# str = "this is string example"
# print(str.startswith('th'))
# print(str.endswith('th'))


"""
isdigit() 判断字符串是否由数字组成，返回 True or False

"""
# str1 = '123a' __name__   __main__
# print(str1.isdigit())
