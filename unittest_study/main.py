'''
测试入口
'''

#找不到 unittest_study 解决方法
import sys
from os.path import abspath,dirname
sys.path.insert(0,dirname(dirname(abspath(__file__))))

import unittest
from unittest_study.testcases.test_demo1 import TestDemo1
from unittest_study.testcases.test_demo2 import TestDemo2


#加载测试用例方法1：class('test')
def get_suite1():
    #实例化测试套件
    suite = unittest.TestSuite()
    #加载测试用例
    suite.addTest(TestDemo1('testdemo1_01'))
    suite.addTest(TestDemo2('testdemo2_01'))
    return suite

# 加载测试用例的方法:3：unittest.TestLoader.loadTestsFromTestCase()
def get_suite2():
    suite=unittest.TestSuite()
    #实例化测试用例加载器
    loder=unittest.TestLoader()
    #加载测试用例
    test1=loder.loadTestsFromTestCase(TestDemo1)
    test2=loder.loadTestsFromTestCase(TestDemo2)
    #将测试用例加载到测试套件
    suite.addTests([test1,test2])
    return suite


#加载测试用例方法3：unittest.TestLoader.discover(start_dir='',pattern='')
def get_suite3():
    suite=unittest.TestSuite()
    loder=unittest.TestLoader()
    #搜索测试用例
    tests=loder.discover(start_dir='./testcases',pattern='test*.py')
    suite.addTests(tests)
    return suite

#运行测试套件
if __name__ == '__main__':
    suite = get_suite3()
    #运行测试套件，将日志保存在report.txt文件
    with open(file='./report.txt',mode='w',encoding='utf-8') as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)