#os模块-操作系统功能模块，可以用来处理文件和目录
import os

#dir()内置函数可以显示模块的所有方法和变量
# print(dir(os))

#控制台中执行命令
#os.name 显示当前使用的平台,nt-windows,posix-linuxs
# print(os.name)

#os.getcwd() 显示当前python脚本工作路径
# print(os.getcwd())

#os.path.abspath(path)  显示当前绝对路径

# os.listdir('dirname') 返回指定目录下的所有文件和目录名
# print(os.listdir('os'))
# print(os.listdir('201912'))

# os.remove('filename')  删除一个文件





#参考地址：https://www.runoob.com/python3/python3-os-file-methods.html