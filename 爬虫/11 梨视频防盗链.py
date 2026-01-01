import requests

url = "https://pearvideo.com/video_1803575"
contID = url.split("_")[1]

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.8151 SLBChan/115 SLBVPV/64-bit",
        "Referer": url
    }

VideoStatusUrl = f"https://pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.0882"
resp = requests.get(VideoStatusUrl, headers=headers)
dic= resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
print(srcUrl)

# https://video.pearvideo.com/mp4/short/20251111/cont-1803574-16066214-hd.mp4
# https://video.pearvideo.com/mp4/short/20251111/1763461430766-16066214-hd.mp4
srcUrl = srcUrl.replace(systemTime, f"cont-{contID}")
print(srcUrl)

with open("./资源/梨视频1.mp4", "wb") as f:
    f.write(requests.get(srcUrl).content)