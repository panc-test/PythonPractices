'''
将生成的斐波那契数列写入csv
'''
import csv
x=int(input('enter a number:'))

#定义一个fio函数生成x以内的所有斐波那契数列
def fio(num):
    n1,n2=0,1
    list=[n1,n2]
    nth=0
    for i in range(0,num):
        nth=n1+n2
        if nth<=num :
            n1=n2
            n2=nth
            list.append(nth)
    return list
#定义一个write_csv函数，
def write_csv(list):
    with open('data.csv','w') as f:
        w=csv.writer(f)
        w.writerow(list)
    f.close()


fio_list=fio(x)
write_csv(fio_list)