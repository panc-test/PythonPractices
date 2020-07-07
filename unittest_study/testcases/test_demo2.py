#接口B的测试用例

import unittest

class TestDemo2(unittest.TestCase):

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

    @unittest.skip('注释：跳过测试')
    def testdemo2_01(self):
        print('testdemo2_01')

    def testdemo2_02(self):
        print('testdemo2_02')


