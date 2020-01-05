'''
生成器
'''

def genartion_func():
    for i in range(10):
        yield i

for x in genartion_func():
    print(x)