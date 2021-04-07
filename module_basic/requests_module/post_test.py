'''
post请求
1、功能提交数据，对数据库执行更新操作
2、请求参数在body中，请求的格式多样性，可以是表单格式，json格式
3、比get请求的数据长度长

'''
import requests

url = 'http://apis.juhe.cn/mobile/get'
token = '80b11be8-cb8f-470a-9f7a-e415a8f1b3be'
body={
    'accesstoken':token,
    'title':'panc-xxxxxxxxx',
    'content':'dhhhhhhhhhhhj',
    'tab':'ask'
}
#post请求的参数可以有2种数据格式
r=requests.post(url=url, data=None, json=body)

assert r.status_code == 200
print(r.json())

