import requests

# url = 'https://p5.music.126.net/obj/wonDlsKUwrLClGjCm8Kx/63627063938/9a0b/9c58/e3f1/06e31cdec3aaad96229b55d7fdbadfff.jpg?imageView&quality=89'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
# }
#
# res = requests.get(url, headers=headers)
# # print(res.content)
#
# with open("../资源/网易云图片1.jpg", "wb") as f:
#     f.write(res.content)

url = "https://m804.music.126.net/20251103173621/d681cc045f4f1a3b94e13c67cc8d3614/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/12577143974/9bf9/d65b/b10a/893c697c85a08ae488483a5c2dbea455.m4a?vuutv=YUjMDm144Z6TqocBFXjWxLiOH2e6oqN+ugZAqKNtmY0htb38X2JGIjuLCmqkgxIZo+tBDZCIAmEphbssHodLs0bsykb4QiTKrLBM83sg0rs=&authSecret=0000019a48fc3da81cfd0a3b1db2beaf&cdntag=bWFyaz1vc193ZWIscXVhbGl0eV9leGhpZ2g"
res2 = requests.get(url)
print(res2.content)

with open("../资源/Underground.mp3", "wb") as f:
    f.write(res2.content)

# url = 'https://vodkgeyttp8.vod.126.net/cloudmusic/IDI0MCEkISEwMCQgMCBhIA==/mv/318001/149d1377ccf314c913d92f736a845a8c.mp4?wsSecret=26c0faa9d1628c10fed9faa18d69145a&wsTime=1762161797'
# res3 = requests.get(url)
#
# with open("../资源/master_of_tide.mp4", "wb") as f:
#     f.write(res3.content)