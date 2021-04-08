'''
接口地址：
https://cnodejs.org/api
get请求
1、功能查询数据，对数据库执行查询操作
2、请求参数在url上可以看到

'''
import requests

#请求地址
url = 'https://cnodejs.org/api/v1/topics'
#请求参数
params = {
    'page':1,
    'tab':'job',
    'limit':5,
    'mdrender':'false'
}
#创建请求
r = requests.get(url,params)
assert r.status_code == 200
print(r.json())
