import requests

# url = " https://www.baidu.com/"
#
# response = requests.get(url)
# print(response)
# # print(response.text)
# print(response.content.decode())

# url = "https://pic.rmb.bdstatic.com/bjh/bc15f555991/250305/1ec44ecff7cd277ccb715eae7d2a5895.jpeg"
# res = requests.get(url)
# print(res.content)
#
# with open("teat1.jpg","wb") as f:
#     f.write(res.content)

# url = "https://q0.itc.cn/q_70/images03/20240309/a2b719342f7b478c8633c0ade4792e46.jpeg"
# res = requests.get(url)
# print(res)
# # print(res.text)
# # print(res.content.decode())
# with open("../资源/test2.jpg", "wb") as f:
#     f.write(res.content)
# print(res.url)
# print(res.request.headers)
# print(res.headers)
# print(res.apparent_encoding)


url = "https://www.baidu.com/"
# response = requests.get(url)
#
# # with open("baidu.html", "w", encoding='utf-8') as f:
# #     f.write(response.content.decode())
#
# content = response.content.decode('utf-8')
# print(len(content))

#构建请求头
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# response = requests.get(url, headers=headers)
response = requests.get(url)
print(response.request.headers)
# print(response.content.decode('utf-8'))
# print(len(response.content.decode('utf-8')))

