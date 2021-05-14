"""
while循环

"""
# while 循环，计算 0 到 9 的累加值
result = 0
num = 1
while num < 10:
    result +=num
    num += 1

print(result)


# # 打印9*9乘法表
# i = 1
# while i < 10 :
#     for j in range(1, i+1) :
#         print('{}*{}={}\t'.format(j, i, i*j), end='')
#
#     print()
#     i +=1