"""
for循环

"""
# for 循环，计算 0 到 9 的累加值
result = 0
for num in range(10):
    result +=num
    # result = result + num

print(result)


# 打印9*9乘法表
for i in range(1,10):   # 第几行
    for j in range(1,i+1):  # 第几列
        print('{}*{}={}\t'.format(j,i,j*i),end='')  # 注意这里是 列*行

    print() # 实现分行输出，不能少