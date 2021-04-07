'''
xlwt模块-往excel文件中写入数据
'''

import xlwt

#创建一个工作簿
wb=xlwt.Workbook()

#新建一个sheet页
sheet=wb.add_sheet(sheetname='xxxx')

#单元格中写入数据
sheet.write(r=2,c=3,label=100)

#保存工作簿
wb.save('./data.xls')

# wb.save('./data.xlsx')