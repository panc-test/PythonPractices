"""
json 模块

"""

import json

data = {
    'name' : 'myname',
    'age' : 100,
}
json_str = json.dumps(data)     # 将dict转换成str类型
print(json_str,type(json_str))