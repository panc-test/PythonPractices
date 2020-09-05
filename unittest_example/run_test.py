"""
运行测试用例
"""

import unittest
import unittest_example.test_register
from BeautifulReport  import  BeautifulReport


# 实例化对象
tr=unittest_example.test_register.TestRegister()
# 第一步，创建一个测试套件
suite = unittest.TestSuite()

# 第二步：将测试用例，加载到测试套件中
loader = unittest.TestLoader()	# 创建一个加载对象
cases=loader.loadTestsFromModule(unittest_example.test_register)
suite.addTests(cases)


if __name__ == '__main__':
    #执行测试套件
    result=BeautifulReport(suite)
    #生成测试报告
    result.report(report_dir='./',filename='report',description='测试报告的注释内容')