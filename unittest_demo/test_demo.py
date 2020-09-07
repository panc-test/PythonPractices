'''
unittest单元测试框架

'''

import unittest

class TestDemo(unittest.TestCase):  #继承TestCase类

    @classmethod    #装饰器
    def setUpClass(cls) -> None:    #所有测试用例执行前的环境准备
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None: #所有测试用例执行结束后的环境恢复
        print('tearDownClass')

    def setUp(self):    #每条测试用例执行前执行
        print('setUp')

    def tearDown(self): #每条测试用例执行后执行
        print('tearDown')

    def testA(self):
        print('testA')

    def testB(self):
        print('testB')

    def testa(self):
        print('testa')

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

#程序主入口
if __name__ == '__main__':
    unittest.main(verbosity=2)

