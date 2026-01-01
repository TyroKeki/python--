from lxml import etree

tree = etree.parse('练习Xpath示例.html')

# result = tree.xpath('/html')
# print(result)

# result = tree.xpath('/html/body/ul/li[1]/a/text()')
# print(result)

# result = tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')
# print(result)

ol_li_list = tree.xpath("/html/body/ol/li")

for li in ol_li_list:
    result = li.xpath("./a/text()")
    print(result)

    result2 = li.xpath("./a/@href")
    print(result2)

result = tree.xpath("//ul/li/a/@href")
print(result)

print(tree.xpath("/html/body/div[1]/text()"))
