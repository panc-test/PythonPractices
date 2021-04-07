'''
从已知的列表中取随机数
'''

from faker import Faker


fake=Faker('zh_CN')

tab_list=['share','ask','dev']
#从tab_list中随机取一个值
tab =fake.sentence(nb_words=1,variable_nb_words=True,ext_word_list=tab_list)
print(tab)

#首字母小写，去掉.