'''
python中 内置函数 __init__方法 和 __new__方法 区别

'''


class display(object):

  def __init__(self, *args, **kwargs):
    print("init")

  def __new__(cls, *args, **kwargs):
    print("new")

a=display()
