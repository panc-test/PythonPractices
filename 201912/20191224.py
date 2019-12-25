#打印输出1-1000之间的所有阿姆斯特朗数,如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。

for num in range(1,1001):
    n=len(str(num)) #求数字num的位数，也是指数
    sum=0
    temp=num
    while temp>0:
        digit=temp%10   #求余数
        sum+=digit**n    #等同于sum=sum+digit**n
        temp=temp//10   #向下取整
    if sum==num:
        print(num)


'''
1=1^1
2=2^1
……
153=1^3+5^3+3^3
370=3^3+7^3+0^3
371=3^3+7^3+1^3
407=4^3+0^3+7^3

'''