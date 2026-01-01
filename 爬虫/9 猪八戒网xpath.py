import requests
from lxml import etree

url = "https://www.zbj.com/fw/?k=saas"
resp = requests.get(url)
print(resp.text)

html = etree.HTML(resp.text)
divs = html.xpath('''//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div''')
#确认总起xpath：//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]
#确认名称xpath：//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/span
#确认公司xpath：//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[5]/div/div/div

for div in divs:
    price = div.xpath('./div/div/div[@class="price"]/span/text()')[0]
    # print(price)

    title = "saas".join(div.xpath('./div/div[3]/div[2]/div/span/text()'))
    # print(title)

    company = div.xpath('''./div/div[5]/div/div/div/text()''')[0]
    # print(company)

    ListOfAll = [price,title,company]
    print(ListOfAll)
