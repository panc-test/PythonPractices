'''
Note！！！

Only cells (including values, styles, hyperlinks and comments) and
certain worksheet attribues (including dimensions, format and properties) are copied.
All other workbook / worksheet attributes are not copied - e.g. Images, Charts.

You also cannot copy worksheets between workbooks.
You cannot copy a worksheet if the workbook is open in read-only or write-only mode.
'''

from openpyxl import Workbook


wb=Workbook()
ws=wb.active
list=[1,2,3,4,5]
ws.append(iterable=list)
#拷贝工作表，注意拷贝之后的sheetname
wb.copy_worksheet(ws)

wb.save('data_20200803.xlsx')

