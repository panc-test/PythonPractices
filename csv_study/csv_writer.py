'''
写入.csv文件
'''

import csv

#列表写入csv文件
def writer1():
    headers = ['username', 'password', 'except_val']
    rows = [('user1', '123456', '登录成功'), ('user1', '', '密码不能为空'), ('', '123456', '用户名不能为空'),
            ('xxxx', 'xxxx', '用户名或密码有误')]

    with open('data2.csv',encoding='utf8', mode='w',newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(rows)

#字典写入csv文件
def writer2():
    headers = ['username', 'password', 'except_val']
    rows = [{"username": "user1", "password": "123456", "except_val": "登录成功"},
            {"username": "user1", "password": "", "except_val": "密码不能为空"},
            {"username": "", "password": "123456", "except_val": "用户名不能为空"},
            {"username": "xxxxx", "password": "xxxx", "except_val": "用户名或密码有误"}]

    with open('data3.csv',encoding='utf8', mode='w',newline='') as f:
        csv_writer = csv.DictWriter(f,headers)
        csv_writer.writeheader()
        csv_writer.writerows(rows)

writer2()


