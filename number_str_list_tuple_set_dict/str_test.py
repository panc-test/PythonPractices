"""
python基础数据类型-字符串 string(不可变数据类型)


"""

"""
format() 方法对字符串进行格式化。
    格式：'{}'.format(args)

"""
# #一个参数
# print('{}'.format('this is example'))
# #多个参数，不指定位置，按默认顺序
# print('{} {}'.format('hello','world'))
# #多个参数，设置指定位置
# print('{0} {0} {1}'.format('hello','world'))
#
# #格式化数字
# print("{:.2f}".format(3.1415926))  #保留2位小数



"""
查找元素方法：
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
replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
    语法：str.replace(old,new,max)
    old -- 将被替换的子字符串。
    new -- 新字符串，用于替换old子字符串。
    max -- 可选字符串, 替换不超过 max 次

"""
str = "this is string example....wow!!! this is really string"
a = str.replace('this','THIS')
print(a)
print(str)


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
1.join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    语法：str.join(sequence)
2.split() 通过指定分隔符对字符串进行切片，返回分割后的字符串列表。
    语法：str.split(sep,maxsplit)
    sep -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    maxsplit -- 分割次数。默认为 -1, 即分隔所有。如果参数 num 有指定值，则分隔 num+1 个子字符串,

"""
# seq = ['www','runoob','com']
# #拼接字符串
# url = '.'.join(seq)
# print(url)
# #分割字符串
# a=url.split(sep='.')
# print(a)


"""
大小写转换：
1.capitalize() 将字符串的第一个字母变成大写,其他字母变小写。
2.title() 方法用于将字符串中每个单词的首字母转为大写，其他字母全部转为小写。
3.upper() 方法用于将字符串中的所有小写字母转换为大写字母。
4.lower() 方法用于将字符串中的所有大写字母转换为小写字母。
注意：
这几张方法都不会改变原始字符串，字符串是不可变的
 
"""
# str = "hello world ABC"
# print(str.capitalize())
# print(str.title())
# print(str.upper())
# print(str.lower())


"""
删除字符：
1.strip()：删除字符串前后（左右两侧）的空格或特殊字符。
2.lstrip()：删除字符串前面（左边）的空格或特殊字符。
3.rstrip()：删除字符串后面（右边）的空格或特殊字符。
    语法：str.strip(chars)
    chars -- 移除的字符序列
注意：
这里的特殊字符指的是制表符（\t）、回车符（\r）、换行符（\n）等。

"""
# str = "  hello world \t "
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())



"""
count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
    语法：str.count(sub, start,end)
    sub -- 搜索的字符
    start -- 字符串开始搜索的位置。默认为第一个字符。
    end -- 字符串中结束搜索的位置。默认为字符串的最后一个位置。

"""
# str = "this is string example"
# print(str.count('s'))
# print(str.count('s',1,5))


"""
encode() 方法以 encoding 指定的编码格式编码字符串。
decode() 方法以 encoding 指定的编码格式解码字符串。

"""
# str = "中文网"
# #编码
# a = str.encode(encoding='UTF-8')
# print(a,type(a))
# #解码
# b = a.decode()
# print(b,type(b))


"""
startswith() 方法用于检索字符串是否以指定字符串开头，如果是返回 True；反之返回 False。
endswith() 方法用于检索字符串是否以指定字符串结尾，如果是则返回 True；反之则返回 False。

"""
# str = "this is string example"
# print(str.startswith('th'))
# print(str.endswith('th'))
