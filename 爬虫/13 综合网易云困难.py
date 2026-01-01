import requests

#token=4876855fb660b434a640dd0eda2e53c7
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
resp = requests.post(url)