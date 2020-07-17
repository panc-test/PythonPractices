'''
ddt-数据驱动模块
@data()可以是列表，元组，字典
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