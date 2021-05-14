"""
open 打开一个文件，并返回一个文件对象

"""
# 打开文件，获取文件对象
f = open(file='./file.txt',mode='w+',encoding='utf-8')
print(f)

# 操作文件对象
print(f.name)
print(f.read()) # 从文件中读取指定的字节数
f.write('hello world')  # 向文件中写入字符串，注意写入的字符字符串格式必须跟打开文件的格式一致


# 关闭文件对象
f.close()