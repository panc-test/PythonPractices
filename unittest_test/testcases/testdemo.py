"""
测试用例
"""

import unittest


class TestDemo01(unittest.TestCase):

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

    def test_04(self):
        print('test_04')

    def test_05(self):
        print('test_05')

    def test_06(self):
        print('test_06')



class TestDemo02(unittest.TestCase):

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

    def test_07(self):
        print('test_07')

    def test_08(self):
        print('test_08')

    def test_09(self):
        print('test_09')






