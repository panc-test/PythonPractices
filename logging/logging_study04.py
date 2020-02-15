'''
Filters筛选logger对象后发送给handler
'''

import logging

logger1 = logging.getLogger('mylogger1')
logger2 = logging.getLogger('mylogger2')

# 创建一个handler，用于写入日志文件
handler = logging.FileHandler('study04.log')

#分别定义日志级别
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.INFO)

#设置日志打印格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#添加打印格式
handler.setFormatter(formatter)

## 定义一个filter
filter=logging.Filter('mylogger1')

##添加filter样式
handler.addFilter(filter)

logger1.addHandler(handler)
logger2.addHandler(handler)


logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')