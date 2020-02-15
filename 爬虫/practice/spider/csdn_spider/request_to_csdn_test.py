import requests
from  urllib import parse


url="https://me.csdn.net/csdngkk"

res_text=requests.get(url=url).text
print(res_text)