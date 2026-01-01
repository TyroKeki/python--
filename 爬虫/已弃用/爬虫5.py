import requests
import random
from fake_useragent import UserAgent
from urllib.parse import  quote, unquote
import time

current_time = int(time.time() * 1000)
print(current_time)

url = "https://fanyi.baidu.com/ait/text/translate"
V_User = UserAgent().random

headers = {
    "User-Agent": V_User,
    "cookie" :
}

post_data = {
    "corpusIds": '[]',
    "detectLang": '""',
    "domain": '"common"',
    "from": 'from_lang',
    "isAi": 'False',
    "isIncognitoAI": 'False',
    "milliTimestamp": 'current_time',
    "needPhonetic": 'False',
    "query": 'query_text',
    "reference": "",
    "sseStartTime": current_time - 73,  # 模拟原始数据的时间差
    "to": 'to_lang'
}

try:
    res = requests.post(url, headers=headers,data=post_data,timeout=10)
    print(f"状态码:{res.status_code}")

    if res.status_code == 200:
        result = res.content.decode('utf-8')
        print(result)
    else:
        print(f"请求失败，状态码: {res.status_code}")

except requests.exceptions.RequestException as e:
    print(f"请求异常: {e}")

