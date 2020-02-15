import requests
import json

# url = "https://www.baidu.com"
url = "https://www.taobao.com"

res = requests.get(url=url)
print(res.text)
