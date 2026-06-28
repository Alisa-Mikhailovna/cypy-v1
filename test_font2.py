import requests
url = "https://fonts.google.com/download?family=Noto+Sans+KR"
resp = requests.get(url, stream=True)
print(f"Status: {resp.status_code}")
print(f"Content-Type: {resp.headers.get('Content-Type')}")
print(f"Content-Disposition: {resp.headers.get('Content-Disposition')}")
print(f"Length: {len(resp.content)} bytes")
