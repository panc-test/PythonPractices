'''
ZipFile-读取指定的zip压缩文件
'''

from zipfile import ZipFile


file_name='./new.zip'
myzip=ZipFile(file=file_name,mode='r')
myzip.printdir()


'''
拓展
ZipFile.extract(member, path=None, pwd=None)
将zip文档内的指定文件解压到指定目录。参数member指定要解压的文件名称或对应的ZipInfo对象；参数path指定了解析文件保存的文件夹；参数pwd为解压密码。

ZipFile.extractall(member, path=None, pwd=None)
解压zip文档中的所有文件到指定目录。参数members的默认值为zip文档内的所有文件名称列表，也可以自己设置，选择要解压的文件名称

ZipFile.setpassword(pwd)
设置zip文档的解压密码。

ZipFile.getinfo(name)
获取zip文档内指定文件的信息。返回一个zipfile.ZipInfo对象，它包括文件的详细信息。

ZipFile.infolist()
获取zip文档内所有文件的信息，返回一个zipfile.ZipInfo的列表
'''