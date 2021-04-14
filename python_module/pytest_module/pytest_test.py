"""
pytest - 单元测试模块
运行方式；
1.命令行模式运行
2.pytest.mian([])

"""
import pytest

#被测函数
def fun(x):
    return x + 1
#测试用例
def test_fun():
    assert fun(1) == 2
#
# if __name__ == '__main__':
#     pytest.main(['-v','pytest_test.py'])
