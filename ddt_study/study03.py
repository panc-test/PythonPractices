'''
ddt-读取yaml文件数据
'''


import unittest
from ddt import ddt,file_data


@ddt
class DDTTest(unittest.TestCase):

    @file_data('./data.yaml')
    def test_get_data(self,start,end,value):

        #将从json文件中读到的数据存放到values中
        values={
            'values_start':start,
            'values_end':end,
            'vlues_value':value
        }

        print('values=',values)


if __name__ == '__main__':
    unittest.main(verbosity=2)
