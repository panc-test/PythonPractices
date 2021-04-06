"""
官方教程：
https://docs.pytest.org/en/stable/contents.html#toc

"""

# 定义一个 add()函数
def add(x,y):
    return x + y

#编写 add（）函数测试方法
def test_add1():
    assert add(1,2) == 5

def test_add2():
    assert add(1.0,2.0) == 3.0

def test_add3():
    assert add('a','b') == 'ab'

def test_add4():
    # 不合理的输入值
    assert add('a',1) == 'a1'
