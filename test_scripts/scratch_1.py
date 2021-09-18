"""
将'a1b2c3d4' 转换成 'abbcccdddd'
思路
1、拆分原始字符串
2、拼接出目标字符串，使用字符串操作 key*value

"""
str = 'a1b2c3d4'


def fun1():
    # 字符串切片，list[start:stop:step]
    str1 = str[::2]
    str2 = str[1::2]
    # print(str1,str2)
    str_new = ''
    for i in range(len(str1)):
        str_new += str1[i] * int(str2[i])  # 注意这里必须加int()

    print(str_new)


def fun2():
    # range() 步长2
    str_new = ''
    for i in range(0, len(str), 2):
        str_new += str[i] * int(str[i + 1])

    print(str_new)


if __name__ == '__main__':
    # fun1()
    fun2()
