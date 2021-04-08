'''
post请求
1、功能提交数据，对数据库执行更新操作
2、请求参数在body中，请求的格式多样性，可以是表单格式，json格式
3、比get请求的数据长度长

'''
import requests

url = 'https://cnodejs.org/api/v1/topics'
token = '693fe588-3168-41a2-90f6-729071ec7303'
body={
    'accesstoken':token,
    'title':'test-测试下一会就删',
    'content':'dhhhhhhhhhhhj',
    'tab':'ask'
}
#post请求的参数可以有2种数据格式
r=requests.post(url=url,json=body)

assert r.status_code == 200
print(r.json())

