# content of test_example.py

import pytest


@pytest.fixture
def error_fixture():
    assert 0    #调用这个方法返回结果失败的意思,调试运行时到此处报错,可以有标记函数还没写完的作用吧

def test_ok():
    print("ok")

def test_fail():
    assert 0

def test_error(error_fixture):
    pass

def test_skip():
    pytest.skip("skipping this test")

def test_xfail():
    pytest.xfail("xfailing this test")

@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass
