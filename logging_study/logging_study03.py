'''
创建2个logger对象，分别发往不同的handler
'''

import logging

#创建logger
logger1 = logging.getLogger('mylogger1')
logger2 = logging.getLogger('mylogger2')

# 创建handler
handler1 = logging.FileHandler('study03.log')   #写入日志文件
handler2 = logging.StreamHandler()  #输出到控制台

#设置输出日志级别
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.INFO)

#设置handler输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

##将logger添加到handler
logger1.addHandler(handler1)
logger2.addHandler(handler2)


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