'''
unittest-单元测试框架
'''

import unittest
from selenium import webdriver


class Utest(unittest.TestCase):
    #每个测试用例执行之前操作
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()    #只能放在这里
        self.driver.maximize_window()
    #每个测试用例执行之后操作
    def tearDown(self) -> None:
        self.driver.quit()
    #测试用例1
    def test01(self):
        self.driver.get('https://cn.bing.com/')
    #测试用例2
    def test02(self):
        self.driver.get('http://39.107.96.138:3000/')


if __name__ == '__main__':
    unittest.main()

