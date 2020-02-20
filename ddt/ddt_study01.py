'''
ddt-数据驱动模块
官网：https://ddt.readthedocs.io/en/latest/example.html
'''

import unittest
from ddt import ddt,data,file_data

@ddt
class TestDDT(unittest.TestCase):

    @data(3,5,1,4)      #测试数据，也可以是函数
    def test_get_data(self,values):
        print('values==',values)

    @file_data('data.yaml')  #注意文件路径
    def test_get_filedata(self,start,end,value):
        print('start==',start)
        print('end==', end)
        print('value==', value)


if __name__ == '__main__':
    unittest.main(verbosity=2)