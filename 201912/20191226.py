#迭代器

list=[1,2,3,4,5]
it=iter(list)    #创建一个迭代器对象
print(it)

next(it)  #迭代一个
print(next(it))

for i in it:
    print('i=',i)