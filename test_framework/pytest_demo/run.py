"""
pytest单元测试框架

"""
import pytest


# 被测函数
def add(x, y):
    return x + y


# 测试用例
def test_add1():
    assert add(1, 2) == 5


def test_add3():
    assert add('a', 'b') == 'ab'


if __name__ == '__main__':
    # pytest.main()
    pytest.main(['run.py'])
