"""
fileinput -读取多个文件流

"""
import fileinput

for line in fileinput.input(files=('file1.txt','file2.txt')):
    print(line)