"""
contextlib -上下文管理器模块

"""
import contextlib


@contextlib.contextmanager
def open_func(file_name):
    # __enter__方法
    print('open file:', file_name)
    file_handler = open(file_name, 'r')

    try:
        yield file_handler
    except Exception:
        print('deal with exception')
    finally:
        # __exit__方法
        print('close file:', file_name)
        file_handler.close()


with open_func('mytest.txt') as f:
    print(f)
    for i in f:
        1/0
        print(i)
