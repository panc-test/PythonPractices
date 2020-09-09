'''
ZipFile-向已有的zip压缩包中添加文件(一)
'''

from zipfile import ZipFile


file_name='./new.zip'
file_list=['Snipaste.png','test_fun.py']
with ZipFile(file=file_name,mode='w') as myzip:    #注意w会删除压缩包内已有的文件
    for f in file_list:
        myzip.write(f)
myzip.printdir()

