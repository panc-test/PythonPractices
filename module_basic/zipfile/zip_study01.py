'''
ZipFile-创建zip压缩文件，并向其中添加指定的文件
zipfile.ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, compresslevel=None, *, strict_timestamps=True)
形参mode值：
'r' 来读取一个存在的文件
'w' 向压缩包中添加文件，删除压缩包内已有的文件，只有新文件
'a' 向压缩包中添加文件，不会删除压缩包内已有的文件，新老文件都存在
'x' 来仅新建并写入新的文件
'''

from zipfile import ZipFile

#创建一个空的压缩文件,并将指定文件添加到压缩包
file_name= 'new.zip'
myzip=ZipFile(file=file_name,mode='w')
file_name= 'test.txt'
myzip.write(filename=file_name)
#将zip文档内的信息打印到控制台上。
myzip.printdir()






