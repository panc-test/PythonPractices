#接口A的测试用例

import unittest

class TestDemo1(unittest.TestCase):

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

    def testdemo1_01(self):
        print('testdemo1_01')

    def testdemo1_02(self):
        print('testdemo1_02')


