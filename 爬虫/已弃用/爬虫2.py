import requests
import random
from fake_useragent import UserAgent
from urllib.parse import  quote, unquote

UAlist = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
]

# print(random.choice(UAlist))
# print(UserAgent().random)


# print(quote('参数')) #字符串
# print(unquote('%E5%8F%82%E6%95%B0')) #%xx
#
# url = 'https://www.so.com/s?q=%E5%AD%A6%E4%B9%A0'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE/13.5.2044.0'
# }
# res = requests.get(url, headers=headers)
# print(res.content.decode())


name = input("请输入关键字:")
kw = {'q': name}

# url = "https://www.so.com/s"
url = f'https://www.so.com/s?q={name}'

V_user = UserAgent().random
headers = {
    'User-Agent': V_user
}

# res2 = requests.get(url,headers=headers,params=kw)
res2 = requests.get(url,headers=headers)

print(res2.content.decode('utf-8'))


