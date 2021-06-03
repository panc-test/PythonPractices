"""
str() 输出字符串，追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
repr() 输出字符串，追求明确性，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用。
ascii() 输出ASCII格式的字符串，如果对象包含非 ASCII 字符，则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符
对象可以是元组、列表、字典、字符串、set()创建的集合

"""
obj = 'aaaaaaa'
print(obj,type(obj))
print("str()：",str(obj),type(str(obj)))
print("repr()：",repr(obj),type(repr(obj)))
print("ascii():",ascii(obj),type(ascii(obj)))