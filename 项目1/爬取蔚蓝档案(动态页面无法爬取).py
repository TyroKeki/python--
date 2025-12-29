import requests
from bs4 import BeautifulSoup

# param = {
#
# }

headers = {
    'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE/13.5.2044.0"
}

url = "https://www.gamekee.com/ba/second/23941"
resp = requests.get(url, headers = headers)
# print(resp.text)

main_page = BeautifulSoup(resp.text, 'html.parser')
alist = main_page.find("div",class_="item-wrapper icon-size-6 item-1fr-12 item-group ba-item-group")
print(alist)

count = len(alist)
print(count)

for a in alist:
    href = a.get("href")
    print(href)
    break

second_url = "https://www.gamekee.com" + href
print(second_url)

resp.close()

resp = requests.get(second_url, headers = headers)
print(resp.text)