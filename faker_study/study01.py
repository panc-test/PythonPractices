'''
faker第三方模块：自动生成测试假数据
官网地址：https://faker.readthedocs.io/en/stable/fakerclass.html
源码地址：https://github.com/joke2k/faker/tree/master/faker/providers
'''

from faker import Faker

#实例化对象，简体中文
fake=Faker('zh_CN')

#设置seed值,可以保持每次执行程序取到的值是一致的
fake.random.seed(1)
# Faker.seed(0)

#for 循环批量生成测试数据
for _ in range(3):
    print(fake.name())
    print(fake.address(),fake.city(),fake.country())
    print(fake.credit_card_number(card_type='visa19'))
    print(fake.phone_number())

