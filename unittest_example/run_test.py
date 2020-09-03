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
# 方式1，添加单条测试用例
# case = tr("test_register_success")	# 创建一个用例对象，注意：通过用例类去创建测试用例对象的时候，需要传入用例的方法名（字符串类型）
# suite.addTest(case)	# 添加用例到测试套件中

# 方式2，添加多条测试用例
# case1 = tr("test_register_success")
# case2 = tr("test_username_isnull")
# suite.addTests([case1, case2])	# 添加用例到测试套件中

# 方式3，添加一个测试用例类
# loader = unittest.TestLoader()	# 创建一个加载对象
# cases=loader.loadTestsFromTestCase(tr)
# suite.addTests(cases)

# 方式4，添加一个模块
loader = unittest.TestLoader()	# 创建一个加载对象
cases=loader.loadTestsFromModule(unittest_example.test_register)
suite.addTests(cases)

# 方式5，指定测试用例的所在的目录路径，进行加载
# loader = unittest.TestLoader()
# cases=loader.discover(start_dir=r"D:\github\Python\unittest_example",pattern="test_case*.py")
# suite.addTests(cases)


if __name__ == '__main__':
    #执行测试套件
    result=BeautifulReport(suite)
    #生成测试报告
    result.report(report_dir='./',filename='report',description='测试报告的注释内容')