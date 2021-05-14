"""
高优意图设置新增接口测试

"""
import requests
import cookies_test
import unittest



class TestIntention(unittest.TestCase):
    """
    高优意图设置接口测试用例

    """
    # 获取cookies
    my_cookies = cookies_test.get_cookies()

    def test_find_intention(self):
        # 意图列表查询
        base_url = "http://sit-saas.chinatopcredit.com/raptor-web/jargon/findIntentionPriority/467"
        params = {
            "name" : "",
            "priority" : 0,
            "pageNum" : 1,
            "pageSize" : 10
        }

        r = requests.get(base_url,params,cookies=self.my_cookies)
        assert r.status_code == 200


    def test_update_intention(self):
        # 编辑意图优先级
        update_url = 'http://sit-saas.chinatopcredit.com/raptor-web/jargon/updateIntentionPriority'
        body = {
            'id':10391,
            'priority':1
        }

        r = requests.post(url=update_url,json=body,cookies=self.my_cookies)
        assert r.status_code == 200


if __name__ == '__main__':
    TestIntention().test_find_intention()