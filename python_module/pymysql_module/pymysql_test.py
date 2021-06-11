"""
mysql数据库操作 - PyMySQL
操作流程：
1.连接数据库
2.使用游标操作数据库
3.关闭数据库

"""

import pymysql

# 连接数据库
db = pymysql.connect(host='rm-uf6761kt70m851725.mysql.rds.aliyuncs.com', user='v40g0dlkpmn5it9l',
                     password='JaCAy3ibN3@+w$iY(9DV8r4#pD8kdzOI', database='raptor_sit', port=3306)

# 操作数据库
cur = db.cursor()  # 游标对象
sql = "SELECT * FROM rpt_intention WHERE jargon_id = '887'"
result = cur.execute(sql)
print(cur.fetchone())
print(cur.fetchmany(size=2))
print(cur.fetchall())  # 注意游标的位置

# 关闭数据库
cur.close()
db.close()
