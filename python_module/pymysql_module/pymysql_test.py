"""
mysql数据库操作 - PyMySQL
操作流程：
    1.连接数据库
    2.创建游标对象
    3.执行sql
    4.获取数据
    5.关闭游标
    6.关闭数据库连接

"""
import pymysql

# 数据库配置
config = {
    'host': 'dbtest2.xhdev.xyz',
    'database': 'loki',
    'port': 3306,
    'user': 'panchao01',
    'password': '4GL9&i*Q@wP'
}

# config = {
#     'host': 'dbtest2.xhdev.xyz',
#     'database': 'loki',
#     'port': 3306,
#     'user': 'panchao01',
#     'password': '4GL9&i*Q@wP',
#     'charset': 'utf8',
#     'cursorclass': pymysql.cursors.DictCursor  # #查询返回变字典模式
# }

# 连接数据库
db = pymysql.connect(**config)

# 创建游标对象
cur = db.cursor()

# 操作数据库sql
sql = "select * from loki.loan_credit_info t where t.create_time like '2021-09-09%' order by t.create_time desc;"

# 执行sql
result = cur.execute(sql)
print(result)

# 获取数据，默认返回结果元组
data1 = cur.fetchone()  # 逐行取出数据，没有数据则返回 None
data2 = cur.fetchone()
data3 = cur.fetchone()
data4 = cur.fetchone()
data5 = cur.fetchone()

print(data1, data2, data3, data4, data5)

# data = cur.fetchmany(size=1)    # 取出多行数据
# print(data)

# data = cur.fetchall()  # 取出所有数据
# print(data)

# 关闭游标
cur.close()
# 关闭数据库连接
db.close()
