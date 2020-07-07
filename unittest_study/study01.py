'''
unittest单元测试框架：
1、测试脚手架 test fixture
2、测试用例  test case
3、测试套件  test suite
4、测试执行器 test runner
5、测试报告  test report

测试用例执行顺序：
0-9
A-Z
a-z
'''

import unittest

class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    #每个测试用例执行之前操作
    def setUp(self):
        print('setUp')

    #每个测试用例执行之后操作
    def tearDown(self):
        print('tearDown')

    #测试用例1
    def test01(self):
        print('testcase01')

    #测试用例2
    def test02(self):
        print('testcase02')

#程序主入口
if __name__ == '__main__':
    unittest.main(verbosity=2)

