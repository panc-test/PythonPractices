"""
编写测试用例测试判断三角形形状的函数Function(A,B,C)

"""


# 被测方法
def function(a, b, c):
    # 判断入参都是数字
    if str(a).isdigit() and str(b).isdigit() and str(c).isdigit():
        # 判断三角形
        if a < b + c and b < a + c and c < a + b:
            if a == b or a == c or b == c:
                return "等腰三角形"
            elif a == b == c:
                return "等边三角形"
            else:
                return "普通三角形"
        else:
            return "无法构成三角形"
    else:
        print("输入数据不合法")


# 测试用例
import unittest


class TestFunction(unittest.TestCase):

    # 一般三角形
    def test_triangle01(self):
        assert function(2, 3, 4) == "普通三角形"

    # 等边三角形
    def test_triangle02(self):
        assert function(2, 2, 1) == "等腰三角形"

    # 等边三角形
    def test_triangle03(self):
        assert function(1, 1, 1) == "等边三角形"
        print(function(1,1,1))

    # 不是三角形
    def test_triangle04(self):
        assert function(1, 2, 7) == "无法构成三角形"

    # 参数有误
    def test_triangle05(self):
        assert function(1, 1, -1) == "输入数据不合法"
        print(function(1,1,-1))


if __name__ == '__main__':
    unittest.main()
