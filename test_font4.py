import requests
url = "https://fonts.googleapis.com/css?family=Noto+Sans+KR"
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'}
resp = requests.get(url, headers=headers)
print(resp.text)
