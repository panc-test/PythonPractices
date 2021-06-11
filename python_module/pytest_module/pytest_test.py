"""
pytest - 单元测试框架
官网教程：
https://docs.pytest.org/en/stable/contents.html#toc


"""
import pytest


# 定义一个 add()函数
def add(x, y):
    return x + y


# 编写 add（）函数测试方法
def test_add1():
    assert add(1, 2) == 5


def test_add3():
    assert add('a', 'b') == 'ab'


if __name__ == '__main__':
    # pytest.main()
    pytest.main(['pytest_test.py'])
