"""
*args--接收列表，元组
**kwargs---接收字典

"""

tuple=(1,2,3)
dicts={'username': 'test', 'password': '123456','repass':'123456'}
list1=[100,200,300]
list2=[{'username': 'test1', 'password': '123456','repass':'123456'},{'username': 'test2', 'password': '222222','repass':'222222'},{'username': 'test3', 'password': '666666','repass':'666666'}]



def fun_dicts(username,password,repass):
    print('username=',username)
    print('password=',password)
    print('repass=',repass)

def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)


fun(*tuple)
print('---------------------------')
fun(*list1)
print('---------------------------')
fun_dicts(**dicts)
print('---------------------------')
fun(*list2)





