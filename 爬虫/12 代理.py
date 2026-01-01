import requests

#116.62.230.32:3128
proxies = {
    "https": "116.62.230.32:3128",
}

resp = requests.get("https://www.baidu.com",proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)

