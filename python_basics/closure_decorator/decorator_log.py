"""
一个简单的日志装饰器

"""
import logging

# 创建一个logger日志记录器对象
logger = logging.getLogger()

# 设置logger日志级别
logger.setLevel("DEBUG")

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# 设置日志去向，输出到控制台
handler = logging.StreamHandler()

# 配置输出的日志格式
handler.setFormatter(formatter)

# 给logging日志记录器对象添加此handler
logger.addHandler(handler)


def log_info(func):
    "日志装饰器"

    def wrapper(*args, **kwargs):
        logger.debug('{} is running'.format(func.__name__))  # 控制台打印输出日志
        func(*args, **kwargs)

    return wrapper


@log_info
def test():
    print('logs')


test()
