"""
使用with上下文管理器来管理mysql数据库

"""

import pymysql


# 定义一个数据库上下文管理器
class DB():

    def __init__(self, config):
        # 连接数据库
        self.db = pymysql.connect(**config)

    def __enter__(self):
        # 创建游标，操作设置为字典类型
        self.cur = self.db.cursor()
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.db.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.db.close()


if __name__ == '__main__':
    # 数据库配置
    config = {
        'host': 'rm-uf6761kt70m851725.mysql.rds.aliyuncs.com',
        'user': 'v40g0dlkpmn5it9l',
        'password': 'JaCAy3ibN3@+w$iY(9DV8r4#pD8kdzOI',
        'database': 'raptor_sit',
        'port': 3306
    }
    # 使用with上下文管理器操作数据库
    with DB(config=config) as db:
        sql = "SELECT * FROM rpt_intention WHERE jargon_id = '887'"
        db.execute(sql)
        print(db)
        print(db.fetchall())
