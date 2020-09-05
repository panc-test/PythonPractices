'''
unittest单元测试框架：
1、测试脚手架 test fixture
2、测试用例  test case
3、测试套件  test suite
4、测试执行器 test runner
5、测试报告  test report

测试用例执行顺序：根据ASCII码的顺序加载测试用例
0-9
A-Z
a-z
'''

import unittest

class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    @unittest.skip('跳过该条测试用例')
    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

    def testA(self):
        print('testA')

    def testa(self):
        print('testa')

    def test03(self):
        print('test03')

    def testB(self):
        print('testB')

#程序主入口
if __name__ == '__main__':
    unittest.main(verbosity=2)

