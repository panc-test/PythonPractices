"""
高优意图设置新增接口测试

"""
import requests
import cookies_test


base_url = "http://sit-saas.chinatopcredit.com/raptor-web/jargon/findIntentionPriority/467"
params = {
    "name" : "",
    "priority" : 0,
    "pageNum" : 1,
    "pageSize" : 10
}
# 获取cookies
my_cookies = cookies_test.get_cookies()

# 意图优先级列表查询
r = requests.get(base_url,params,cookies=my_cookies)
print(r)
assert r.status_code == 200
print(r.json())
