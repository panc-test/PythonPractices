"""
fixture - 夹具,可以作为参数传给测试用例
参考地址：
https://www.cnblogs.com/sy_test/p/12325254.html

"""
import pytest

#默认scope="function"，fixture在每个测试用例开始前运行一次
@pytest.fixture()
def funa():     #命名不用test开头，跟测试用例区分开
    print("\n开始执行function")
    a = 'su'
    return a

# fixture为class级别的时候，fixture只在此class里所有用例开始前执行一次
@pytest.fixture(scope='class')
def funb():
    print("\n开始执行class")
    b = '100'
    return b

def test_fixture(funa):     #注意这里是直接把函数名作为参数传入的
    print("执行测试用例test_fixture")
    assert funa == 'su'

@pytest.mark.usefixtures('funa')    #使用mark标记要执行的测试用例，usefixture无法获取到fixture返回值
def test_usefixture():
    print("执行测试用例test_usefixture")


class TestFixture:

    def test_fixture_01(self,funa,funb):
        print("执行测试用例test_fixture_01")
        assert funa == 'su'
        assert funb =='100'

    def test_fixture_02(self,funa,funb):
        print("执行测试用例test_fixture_02")
        assert funa == 'su'
        assert funb == '100'

if __name__ == '__main__':
    pytest.main(['-v','-s','pytest_fixture_test.py'])