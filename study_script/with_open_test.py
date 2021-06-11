"""
读取文件file1.txt ，写入到文件 file2.txt 中

"""
# 方法1
with open('file1.txt', 'r') as read_file, open('file2.txt', 'w') as write_file:
    for line in read_file:
        write_file.write(line)


# # 方法2
# import contextlib
#
# print(dir(contextlib))  # python3已经不支持nested
#
# with contextlib.nested(open('file1.txt', 'r'), open('file2.txt', 'w')) as (read_file, write_file):
#     for line in read_file:
#         write_file.write(line)
