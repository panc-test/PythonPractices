"""
pickle -文件处理模块，他可以将对象转换为一种可以传输或存储的格式
1.任意对象和二进制对象转换 dumps,loads
2.任意对象和二进制文件转换 dump,load

"""
import pickle

# 将python对象转换成二进制对象
lst = [1,2,3]
p1 = pickle.dumps(lst)
print(p1)


# 将二进制对象转换成python对象
p2 = pickle.loads(p1)
print(p2)


# # 将python对象转换成二进制文件
# str = "aaabbbbbbbbbbbbccccccccccccccccc"
# with open('file.txt', 'wb') as f:
#     pickle.dump(obj=str, file=f)


# # 将二进制文件转换成python对象
# with open('file.txt','rb') as f:
#     print(pickle.load(f))