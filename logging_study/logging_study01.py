'''
basicConfig()函数-基础日志模块
'''

import logging

logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='study01.log',
                    filemode='w')
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('this is error message')
logging.critical('this is cirtical message')


'''
logging_study.basicConfig函数各参数:

level: 设置日志级别，默认为logging.WARNING,低于该级别的就不输出了，这时候，如果需要显示低于WARNING级别的内容，可以引入NOTSET级别来显示。
    日志级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
    DEBUG:详细信息，一般只在调试问题时使用。
    INFO :证明事情按预期工作。
    WARNING :某些没有预料到的事件的提示，或者在将来可能会出现的问题提示。例如：磁盘空间不足。但是软件还是会照常运行。
    ERROR:由于更严重的问题，软件已不能执行一些功能了。
    CRITICAL :严重错误，表明软件已不能继续运行了。

format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
 %(asctime)s: 打印日志的时间
 %(filename)s: 打印当前执行程序名
 %(lineno)d: 打印日志的当前行号
 %(levelname)s: 打印日志级别名称
 %(message)s: 打印日志信息
 %(levelno)s: 打印日志级别的数值
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(funcName)s: 打印日志的当前函数
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID

datefmt: 指定时间格式，同time.strftime()
filename: 指定日志文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
style:	如果指定了格式，则对格式字符串使用此样式。
    ’%’ 用于 printf 样式
    ’{’ 用于 str.format()
    ’$’ 用于 string。默认为“%”。
stream: 使用指定的流初始化 StreamHandler。注意，此参数与 filename 不兼容——如果两者都存在，则会抛出 ValueError。
handlers: 如果指定，这应该是已经创建的处理程序的迭代，以便添加到根日志程序中。
    任何没有格式化程序集的处理程序都将被分配给在此函数中创建的默认格式化程序。
    注意，此参数与 filename 或 stream 不兼容——如果两者都存在，则会抛出 ValueError。
'''