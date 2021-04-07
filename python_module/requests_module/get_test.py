'''
get请求
1、功能查询数据，对数据库执行查询操作
2、请求参数在url上可以看到
接口地址：
https://www.juhe.cn/docs
http://hn216.api.yesapi.cn/docs.php

'''
import requests

#接口请求地址
url = 'http://hn216.api.yesapi.cn/'
#请求参数（不能有空额，数据类型）
params={
    's':'App.Common_Phone.QueryLocation',
    'app_key':'363CF6F2AC7C0290EE53329F28ADFD68',
    'phone':'15221738510',
    # 'return_data':'0',
    # 'sign':'6A64BDEA3624F6E36F78FFD4DCA8768B'
}
r=requests.get(url,params)
assert r.status_code == 200
print(r.json())