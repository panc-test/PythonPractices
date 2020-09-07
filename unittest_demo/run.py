
import unittest


#封装测试套件方法
def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()  #loader加载器
    tests = loader.discover(start_dir='./testcases',pattern='test*.py')
    suite.addTests(tests)   #将多个测试用例加载到测试套件
    return suite

# 运行测试套件，并输出文本测试报告
if __name__ == '__main__':
    suite = suite()
    with open(file='./report/report.txt',mode='a') as file:
        runner = unittest.TextTestRunner(verbosity=2,stream=file)   #文件流
        runner.run(suite)
        file.close()

