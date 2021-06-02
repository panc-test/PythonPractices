"""
高优意图设置新增接口测试

"""
import unittest
import requests
import get_cookies


class TestIntention(unittest.TestCase):
    """
    高优意图设置接口测试用例

    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        方案一：获取cookies
        方案二：登录成功，并保存session会话状态
        """
        # cls.my_cookies = get_cookies.get_cookies()
        cls.my_header = get_cookies.get_cookies()
        print(cls.my_header)

    @classmethod
    def tearDownClass(cls) -> None:
        """
        登出操作
        """
        pass

    def test_find_intention(self):
        # 高优意图列表查询
        find_url = "http://sit-saas.chinatopcredit.com/raptor-web/jargon/findIntentionPriority/467"
        params = {
            "name" : "",
            "priority" : 0,
            "pageNum" : 1,
            "pageSize" : 10
        }
        r = requests.get(url=find_url,params=params,headers=self.my_header)
        assert r.status_code == 200

    def test_update_intention(self):
        # 编辑意图优先级
        update_url = 'http://sit-saas.chinatopcredit.com/raptor-web/jargon/updateIntentionPriority'
        body = {
            'id':10391,
            'priority':1
        }

        r = requests.post(url=update_url,json=body)
        assert r.status_code == 200


if __name__ == '__main__':
    TestIntention().test_find_intention()