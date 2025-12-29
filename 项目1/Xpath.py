from lxml import etree

tree = etree.parse("b.html")
# result = tree.xpath('/html/body/ul/li[1]/a/text()')
result = tree.xpath("/html/body/ol/li/a[@href = 'dapao']/text()")
# print(result)


ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    result = li.xpath("./a/text()")
    print(result)
    result2 = li.xpath("./a/@href")
    print(result2)

