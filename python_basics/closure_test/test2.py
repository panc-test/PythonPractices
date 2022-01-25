"""
闭包的应用实例

"""


# 使用闭包计算一个数的 n 次幂
def math_power(power):
    def math_base(base):
        return base ** power

    return math_base


# 计算 2 的平方
print(math_power(2)(2))

# 计算 2 的立方
print(math_power(3)(2))
