"""
读取存放在文件中的cookies,并转换成字典格式

"""
# 读取存放cookies的文件
def get_my_cookies():
    """
    read the cookies file,get dict type cookies

    """
    f = open(r'cookies.txt', 'r')

    my_cookies = {}

    for line in f.read().split(';'):

        name, value = line.strip().split('=', 1)   #去除空格，分割字符串，只分割一次

        my_cookies[name] = value    # 将cookies添加到字典中
    # print(my_cookies)
    return my_cookies


if __name__ == '__main__':
    get_my_cookies()