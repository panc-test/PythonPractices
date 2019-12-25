#调用os，csv模块
import os,csv

#获取test.csv文件路径
print(os.getcwd())     #getcwd（）方法？
filepath=os.path.join(os.getcwd(),'data','test.csv')
print(filepath)

#打开csv文件
f=open(filepath)

#读取csv文件
r=csv.reader(f)
print(r)

#迭代，将读取的文件写入到列表中
file_list=[]
for i in r:
    file_list.append(i)
print(file_list)
