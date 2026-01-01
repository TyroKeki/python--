import requests
import random
from fake_useragent import UserAgent
from urllib.parse import  quote, unquote

url = "https://fanyi.baidu.com/mtpe-individual/transText"
V_User = UserAgent().random
headers = {
    "User-Agent": V_User,
}
try:
    res = requests.get(url, headers=headers,timeout=10)
    print(f"状态码:{res.status_code}")

    if res.status_code == 200:
        with open("../资源/百度翻译.html", "w",encoding='utf-8') as f:
            f.write(res.content.decode('utf-8'))
    else:
        print(f"请求失败，状态码: {res.status_code}")

except requests.exceptions.RequestException as e:
    print(f"请求异常: {e}")

