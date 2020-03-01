'''
ZipFile-向已有的zip压缩包中添加文件(二)
'''

from zipfile import ZipFile


file_name='./new.zip'
file_list=['Snipaste.png','test.txt']
with ZipFile(file=file_name,mode='a') as myzip:    #注意a不会覆盖掉已有的压缩文件
    for f in file_list:
        myzip.write(f)
myzip.printdir()

