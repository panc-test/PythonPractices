"""
流程控制：
顺序结构，分支结构，循环结构
什么时候表达式的值是“真”，“假”

"""
# # if 语句
# con = True
#
# if con:
#     print("条件为真，执行if语句")
#
# print("条件为假，不执行if语句")




# # if...else... 语句
# con = False
#
# if con:
#     print("条件为真，执行if语句")
# else:
#     print("条件为假，执行else语句")





# # if...elif...else... 语句
# if conditon_1:
#     print("条件1为真")
#
# elif conditon_2:
#     print("条件1为假，条件2为真")
#
# elif conditon_n:
#     print("条件1，条件2，条件n-1都为假，条件n为真")
#
# else:
#     print("条件1，条件2，条件n都为假")




# for 循环，遍历数组
# for i in range(5):
#     print(i)



# while 循环,注意死循环
# num = 1
# print("输入数字大于10跳出循环")
# while num <= 10:
#     print(num)
#     num += 1



# 嵌套循环结构,打印九九乘法表
i = 1
while i < 10 :  # 第几行

    for j in range(1, i+1) :    # 第几列
        print('{}x{}={}\t'.format(j, i, i*j), end='')

    print()     # 注意这里不能少
    i +=1
