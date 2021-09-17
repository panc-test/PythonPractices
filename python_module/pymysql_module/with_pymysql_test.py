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
        'host': 'dbtest2.xhdev.xyz',
        'database': 'loki',
        'port': 3306,
        'user': 'panchao01',
        'password': '4GL9&i*Q@wP'
    }
    # 使用with上下文管理器操作数据库
    with DB(config=config) as db:
        sql = "select * from loki.loan_credit_info t where t.create_time like '2021-09-09%' order by t.create_time desc;"
        db.execute(sql)
        print(db)
        print(db.fetchone())
