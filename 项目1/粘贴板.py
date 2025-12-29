import requests

param = {
        'q' : '二次元'
}
url = "https://image.so.com/i"
resp = requests.get(url, params=param)