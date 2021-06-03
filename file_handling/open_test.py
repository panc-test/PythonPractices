"""
文件操作
1.open（）
2.上下文管理器 with...as...

"""
# f = open('file.txt','w')
# f.write("aaaaaaaaaaaa")
# f.close()
#
#
# r = open('file.txt','r')
# print(r.read())
# f.close()


with open('file.txt','r') as f:
    print(f.read())
