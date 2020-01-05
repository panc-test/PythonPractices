'''
斐波那契数列
'''

num=int(input('请输入斐波那契数列个数：'))
n1=0
n2=1
counter=2
if num<=0:
    print("输入非法")
elif num==1:
    print(n1)
else:
    print("斐波那契数列：")
    print(n1,',',n2,end=',')
    while num>counter:
        nth=n1+n2
        print(nth,end=',')
        n1=n2
        n2=nth
        counter+=1