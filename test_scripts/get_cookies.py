"""
获取登录成功后的cookies

"""
import requests

def get_cookies():
    # 实例化一个session对象,保持会话状态
    session = requests.session()

    # 登录
    url = 'http://sit-saas.chinatopcredit.com/auth-api/login'
    body = {
        "loginName": "057776@ztx",
        "loginPwd": "Da11431050"
    }
    r = session.post(url,body)
    assert r.status_code == 200

    if r.status_code == 200:
        # 发短信
        url = 'http://sit-saas.chinatopcredit.com/auth-api/login/sms-send'
        body = {
            "mobileNo": "15221738510"
        }
        re =session.post(url,body)
        assert re.status_code == 200

        if re.status_code == 200:
            # 验证短信
            url = 'http://sit-saas.chinatopcredit.com/auth-api/login/sms-verify'
            body = {
                "mobileNo": "15221738510",
                "verifyCode": "888888"
            }
            res = session.post(url, body)
            assert res.status_code == 200
            # print(res.request.headers)
            # print(res.headers)
            return res.request.headers


if __name__ == '__main__':
    get_cookies()