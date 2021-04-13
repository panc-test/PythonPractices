"""
pytest_html 生成测试报告的插件
命令行：
pytest -v pytest_html_test.py --html=report/report.html

"""

def add(x,y):
    return x+y

class TestAdd():

    def test_add1(self):
        assert add(1,2) == 3

    def test_add2(self):
        assert add(1,3) == 0

    def test_add3(self):
        assert add('a','b') == 'ab'


