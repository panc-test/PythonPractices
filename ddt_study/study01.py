'''
ddt-数据驱动模块
数据中的每个值都将作为单个参数传递给测试方法
'''

import unittest
from ddt import ddt,data

data1={
    "start": 0,
    "end": 2,
    "value": 1
    }
data2= {
    "start": -2,
    "end": 0,
    "value": -1
    }

@ddt
class TestDDT(unittest.TestCase):

    @data(data1,data2)
    def test_get_data(self,values):
        #将data()值传给values
        print('values==',values)


if __name__ == '__main__':
    unittest.main(verbosity=2)