import requests
url = "https://fonts.google.com/download?family=Noto+Sans+KR"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
resp = requests.get(url, headers=headers, stream=True)
print(f"Status: {resp.status_code}")
print(f"Content-Type: {resp.headers.get('Content-Type')}")
print(f"Length: {len(resp.content)} bytes")
