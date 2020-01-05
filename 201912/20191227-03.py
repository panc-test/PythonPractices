'''
迭代器-阿姆斯特朗数
'''
import sys
num=int(input('请输入数字:'))
n=len(str(num))   #获取输入值的位数
list=list(str(num))  #将输入值转化成列表
it=iter(list)   #创建迭代器
sum=0
while True:
    try:
        sum+=int(next(it))**n
    except StopIteration as identifier:
        if sum==num:
            print('num %d 是阿姆斯特朗数'%num)
        else:
            print('num %d 不是阿姆斯特朗数'%num)
        sys.exit()
