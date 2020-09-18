'''
requests_study-post请求
1、功能提交数据，对数据库执行更新操作
2、请求参数在body中，请求的格式多样性，可以是表单格式，json格式
3、比get请求的数据长度长
'''

import requests_study
base_url='http://49.233.108.117:3000/api/v1'
token='80b11be8-cb8f-470a-9f7a-e415a8f1b3be'
#发布话题
body={
    'accesstoken':token,
    'title':'panc-xxxxxxxxx',
    'content':'dhhhhhhhhhhhj',
    'tab':'ask'
}
#post请求的参数可以有2种数据格式
r=requests_study.post(url=base_url + '/topics', data=None, json=body)

print('响应码：',r.status_code)
print('响应体：',r.json())

