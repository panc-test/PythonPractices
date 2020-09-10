# content of test_tmpdir.py
"""
fixture是pytest中的一个特性，fixture可以请求任意资源。
pytest --fixtures查看可用fixture列表，fixture的tmpdir能返回一个唯一的临时目录路径
tmpdir
    Return a temporary directory path object
    which is unique to each test function invocation,
    created as a sub directory of the base temporary
    directory.  The returned object is a `py.path.local`_
    path object.

    .. _`py.path.local`: https://py.readthedocs.io/en/latest/path.html

"""



def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0
