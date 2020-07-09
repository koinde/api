import base64
import hashlib
import hmac
import json
import time
import requests

#generate keys from https://www.koinde.com/user-account/api-key/
API_KEY = "<YOUR_API_KEY>" 
API_SECRET = "<YOUR_API_SECRET>=="


def authenticate():
    private_key = base64.b64decode(API_SECRET)
    stamp = str(int(time.time())*1000)
    data = (API_KEY + stamp).encode('utf-8')
    signature = base64.b64encode(hmac.new(private_key , data , hashlib.sha256).digest())
    headers = {
        "X-PCK":API_KEY,
        "X-Stamp":stamp,
        "X-Signature":signature,
        "Content-Type":"html/text",
        'referer':"https://www.google.com",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    }
    return headers

url = "https://koinde.com/api/v1/update-ad"

dict = {
  "ad-id": 100,
  "price": 8800,
  "status": "active", # | "passive"
 }
resp = requests.get(url=url, data=json.dumps(dict), headers=authenticate())
data = resp.json()

print(data)
