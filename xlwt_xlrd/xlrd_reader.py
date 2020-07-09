'''
xlrd模块-读取excel文件
'''

import xlrd

#读取工作簿
wb=xlrd.open_workbook('data.xls')

#读取工作表
sheet=wb.sheets()[0]

#读取单元格
value1=sheet.cell_value(rowx=2,colx=3)
print(value1)