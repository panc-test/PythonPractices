'''
requests_study-get请求
1、功能查询数据，对数据库执行查询操作
2、请求参数在url上可以看到
'''

import requests_study

#主题首页

#接口请求地址
base_url='http://49.233.108.117:3000/api/v1'

#请求参数（不能有空额，数据类型）
params={
    'page':1,
    'tab':'share',
    'limit':1,
    'mdrender':'false'
}
r=requests_study.get(url=base_url + '/topics', params=params)

print('服务器响应状态码：',r.status_code)
assert r.status_code==200

json_data=r.json()
print('返回体json文件格式：',json_data)
print('success的值：',json_data['success'])
print('id值：',json_data['data'][0])  #注意data值是个列表不是字典