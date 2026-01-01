import requests
import re

domain = "https://www.dytt8899.com/"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.8151 SLBChan/115 SLBVPV/64-bit"
    }

resp = requests.get(domain,verify=False,headers=headers)
resp.encoding = "gb2312"
# print(resp.text)

obj1 = re.compile(r"2025必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"<a href='(?P<herf>.*?)'",re.S)
obj3 = re.compile(r"<title>【(?P<name>.*?)】迅雷下载_电影天堂</title>"
                  r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)</a></td>',re.S)

result1 = obj1.finditer(resp.text)
child_herf_list = []
for it in result1:
    ul = it.group('ul')
# print(ul)

result2 = obj2.finditer(ul)
for itt in result2:
    child_herf =domain+itt.group('herf').strip("/")
    child_herf_list.append(child_herf)
    # print(itt.group('herf'))

#提取子页面内容
for herf in child_herf_list:
    child_resp = requests.get(herf,verify=False,headers=headers)
    child_resp.encoding = "gb2312"
    # print(child_resp.text)
    result3 = obj3.finditer(child_resp.text)
    for ittt in result3:
        print(ittt.group('name'))
        print(ittt.group('download'))
    break

resp.close()




