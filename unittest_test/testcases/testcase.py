"""
测试用例
"""

import unittest


class TestCase(unittest.TestCase):  #定义一个测试类，继承unittest模块的TestCase类

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_01(self):
        print('test_01')

    def test_02(self):
        print('test_02')

    def test_03(self):
        print('test_03')


#运行测试用例
# if __name__ == '__main__':
#     unittest.main()



