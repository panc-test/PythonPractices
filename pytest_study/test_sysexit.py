# content of test_sysexit.py

"""
pytest运行test_mytest的时候，抛出异常，调用fun()方法退出程序

"""
import pytest


def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()


