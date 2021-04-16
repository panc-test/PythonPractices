"""
mark - 标记函数，用来管理侧测试用例,执行冒烟测试用例
官网地址：
https://www.osgeo.cn/pytest/mark.html#mark
命令行模式：
python -m "mark标记" .py文件
pytest -v -m login pytest_mark_test.py

"""
import pytest

#登录功能测试类
@pytest.mark.login
class TestLogin():

    def test_login_sucess(self):
        print('login success')

    def test_login_failed(self):
        print('login failed')

#登出功能测试类
@pytest.mark.logout
class TestLogout():

    def test_logout_sucess(self):
        print('logout success')

    def test_logout_failed(self):
        print('logout failed')
