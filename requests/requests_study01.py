'''
requests-接口请求模块
'''

import requests

url='http://39.107.96.138:3000/api/v1/topics'
#参数是字典形式
params={'page':1,'tab':'share','limit':1,'mdrender':'false'}

r=requests.get(url,params)
print(r)
response=r.json()

print(r.json())
print(response['success'])

'''
print(r.url)
print(r.status_code)
print(r.encoding)
print(r.cookies)

print(r.headers)
print(r.content)

print(r.text)

'''