'''
读取.csv文件
'''

import csv
from collections import namedtuple

#将csv文件读取到列表
def reader1():
    with open(file='./data1.csv',mode='r',encoding='utf-8',newline='') as f:
        csv_reader=csv.reader(f)
        # next(csv_reader)
        for row in csv_reader:
            print(row)
    return row

#将csv文件读取到元组
def reader2():
    with open(file='./data1.csv',mode='r',encoding='utf-8',newline='') as f:
        csv_reader=csv.reader(f)
        head=next(csv_reader)
        Row=namedtuple('Row',head)
        for i in csv_reader:
            row=Row(*i)
            print(row)
    return row


#将csv文件读取到字典
def reader3():
    with open(file='./data1.csv',mode='r',encoding='utf-8',newline='') as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            print(row)
    return row


reader2()