"""
pytest - 单元测试模块

"""
import pytest

#被测函数
def fun(x):
    return x + 1
#测试用例
def test_fun():
    assert fun(1) == 2

