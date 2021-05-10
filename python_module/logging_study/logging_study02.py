'''
logging日志框架-logger,formatter,filter,handler
'''

import logging

#创建一个logger对象
logger = logging.getLogger()

#设置logger日志级别
logger.setLevel(logging.NOTSET)

#设置日志去向
handler=logging.FileHandler(filename='study02.log', encoding='utf-8',)

#设置实际输入到日志文件的日志级别
handler.setLevel(logging.ERROR)

#设置日志格式
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)

#给logger对象添加日志去向
logger.addHandler(handler)

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')
logger.error('this is error message')
logger.critical('this is cirtical message')




