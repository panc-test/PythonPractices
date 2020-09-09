import pytest

#功能函数
def multiply(a,b):
    return a * b

class TestMultiply:
#=======fixtures========
    @classmethod
    def setup_class(cls):
        print('setup_class==============================>')

    @classmethod
    def teardown_class(cls):
        print('teardown_class==========================>')

    def setup(self):
        print('setup======================================>')

    def teardown(self):
        print('teardown===================================>')

    def test_mu(self):
        multiply(2,3) == 6