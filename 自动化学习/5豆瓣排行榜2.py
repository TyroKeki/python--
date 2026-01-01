import requests
import re
import csv

url = "https://movie.douban.com/top250?"
for pages in range(4):
    num1 = pages * 25

    params = {
    "start": num1
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.8151 SLBChan/115 SLBVPV/64-bit"
    }

    resp = requests.get(url,headers=headers,params=params)
    page_content= resp.text

    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                            r'</span>.*?<p>.*?<br>(?P<year>.*?)&nbsp'
                            r'.*?<span class="rating_num" pro'
                            r'perty="v:average">(?P<score>.*?)</span>'
                            r'.*?<span>(?P<num>.*?)</span>',re.S)

    result = obj.finditer(page_content)

    f = open("../爬虫a/data.csv","a",encoding="gbk",newline="")
    csvwriter = csv.writer(f)

    for i in result:
        # print(i.group("name"))
        # print(i.group("score"))
        # print(i.group("num"))
        # print(i.group("year").strip())
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())

    f.close()
    print(f"第{pages}页")
print("总任务已完成")