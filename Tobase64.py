
import base64
import json
 
with open("002.png", 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    data = {
    'Pic' : s,
    "positionNum":"10IST13040109"
    }
 
    json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)


