"""
numpy模块 —— 数据分析

"""

import numpy

#创建矩阵
array = numpy.array([[1,2,3],[4,5,6]])
print(array,'\n',type(array))
#矩阵维度
print(array.ndim)
#行数和列数
print(array.shape)
#元素个数
print(array.size)