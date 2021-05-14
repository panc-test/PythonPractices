"""
break和continue关键字用法

"""
# # break 跳出当前循环体
# for i in range(5):
#     if i == 3:
#         print("遇到3跳出当前循环体")
#         break
#     print(i)


# continue 跳过此次循环
for i in range(5):
    if i == 3:
        print("跳过数字3")
        continue
    print(i)



