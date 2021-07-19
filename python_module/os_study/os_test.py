"""
os模块-用来处理文件和目录

"""
import os

print(os.getcwd())  # 打印输出前python脚本工作的目录路径

cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)

my_path = os.walk(cur_path)
print(my_path)

for i in my_path:
    print(i)