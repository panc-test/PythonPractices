"""
pypinyin ——第三方模块,将汉字转拼音
https://pypi.org/project/pypinyin/

"""
from pypinyin import lazy_pinyin,Style,pinyin

p = pinyin("汉字")
py = lazy_pinyin(hans='汉字',style=Style.NORMAL)

print(p)
print(py)

s = ''
for i in py:
    s += ''.join(i)
    # s = s+''.join(i)

print(s)