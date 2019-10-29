
# -*- coding: utf-8 -*-
import base64
import json
import cv2 as cv

filename = input("请输入待识别图片名：")
with open(filename, 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    data = {
    'Pic' : s,
    "positionNum":"10IST13040109"
    }
 
    json_str = json.dumps(data)

import http.client,urllib.parse

headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("47.112.194.11",8095)
conn.request('POST', '/getMeter', json_str, headers)
response = conn.getresponse()
print(response.status, response.reason)
res_data = response.read().decode('utf-8')

# res = str(data)
result = json.loads(res_data)

#解析返回结果
returnPic = result["Pic"]
imgdata=base64.b64decode(returnPic)
rpfn = 'return%s.jpg' % (filename[0:3])
file=open(rpfn,'wb')
file.write(imgdata)
file.close() 
# cv.imshow('returndata',return.jpg)


print(result["Data"])
conn.close()



#单表positionNum：10IST13040109
#多表positionNum：10IST13040121





