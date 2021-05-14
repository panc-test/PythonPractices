"""
流程控制：
顺序结构，分支结构，循环结构
什么时候表达式的值是“真”，“假”

"""
# # if 语句
# con = False
# if con:
#     print("条件为真，执行if语句")
#
# print("条件为假，不执行if语句")



# # if...else... 语句
# con = True
# if con:
#     print("条件为真，执行if语句")
# else:
#     print("条件为假，执行else语句")



# # if...elif...else... 语句
# con1 = False
# con2 = False
# if con1:
#     print("条件1为真")
# elif con2:
#     print("条件1为假，条件2为真")
# else:
#     print("所有条件都为假")



# # for 循环，计算 0 到 9 的累加值
# result = 0
# for num in range(10):
#     result +=num
#     # result = result + num
#
# print(result)




# # while 循环，计算 0 到 9 的累加值
# result = 0
# num = 1
# while num < 10:
#     result +=num
#     num += 1
#
# print(result)



# # break 跳出当前循环体
# for i in range(5):
#     if i == 3:
#         print("遇到3跳出当前循环体")
#         break
#
#     print(i)


# # continue 跳过此次循环
# for i in range(5):
#     if i == 3:
#         print("跳过数字3")
#         continue
#
#     print(i)



# # for...for...嵌套循环打印9*9乘法表
# for i in range(1,10):   # 第几行
#     for j in range(1,i+1):  # 第几列
#         print('{}*{}={}\t'.format(j,i,j*i),end='')  # 注意这里是 列*行
#     print() # 实现分行输出，不能少





# # while...for...嵌套循环打印9*9乘法表
# i = 1
# while i < 10 :
#     for j in range(1, i+1) :
#         print('{}*{}={}\t'.format(j, i, i*j), end='')
#     print()
#     i +=1
