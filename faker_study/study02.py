'''
练习：给接口 post /topics 新建主题生成一批测试数据，保存在excel文件中
'''

from faker import Faker
from openpyxl import Workbook


#实例化对象
fake=Faker('zh_CN')
wb=Workbook()
ws=wb.active

#生成接口入参的测试数据
tab_list=['share','ask','dev']

accesstoken ='1f2ec36d-8e81-4841-84a8-5edf30b39b7b'
tab =fake.sentence(nb_words=1,variable_nb_words=True,ext_word_list=tab_list)
title =fake.sentence()
content =fake.text()


print(tab,title)


#将测试数据保存到excel文件中



#保存工作簿
