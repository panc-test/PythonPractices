"""
程序主入口，运行测试用例，生成测试报告

1、实例化一个测试套件
2、加载测试用例到测试套件
3、运行测试套件
4、生成测试报告

"""
import unittest
import unittest_test.testcases.testdemo
from unittest_test.testcases.testcase import TestCase
from unittest_test.testcases.testdemo import TestDemo01,TestDemo02


#定义测试套件，并加载测试用例
def suite1():
    # 测试套件
    suite = unittest.TestSuite()
    #加载测试用例
    suite.addTest(TestCase('test_01'))
    suite.addTest(TestCase('test_02'))
    return suite

#加载多个测试用例
def suite2():
    suite = unittest.TestSuite()
    tests = [TestCase('test_02'),TestCase('test_03'),TestDemo01('test_05')]
    suite.addTests(tests)
    return suite

#使用loader加载器，加载指定类中的所有测试用例,一次只能加载一个测试类
def suite3():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test1 = loader.loadTestsFromTestCase(TestCase)
    test2 = loader.loadTestsFromTestCase(TestDemo02)
    tests = [test1,test2]
    suite.addTests(tests)
    return suite

#使用loader加载器，加载指定模块的所有测试用例
def suite4():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()       #加载器
    tests = loader.loadTestsFromModule(unittest_test.testcases.testdemo)
    suite.addTests(tests)
    return suite

#根据给定的字符串来获取测试用例套件，字符串可以是模块名，测试类名，测试类中的测试方法名，或者一个可调用的是实例对象
def suite5():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()       #加载器
    tests = loader.loadTestsFromName('unittest_test.testcases.testdemo.TestDemo02')
    suite.addTests(tests)
    return suite

#与name功能相同，只不过接受的是字符串列表
def suite6():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()       #加载器
    tests = loader.loadTestsFromNames(['unittest_test.testcases.testcase','unittest_test.testcases.testdemo'])
    suite.addTests(tests)
    return suite


#运行测试套件,生成测试报告
if __name__ == '__main__':
    suite = suite6()
    with open(file='./report',mode='a') as file:
        runner = unittest.TextTestRunner(verbosity=2,stream=file)
        runner.run(suite)




