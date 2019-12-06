#python 2.7
import requests,json

#go to https://www.koinde.com/user-account/api-key/ create api key and paste below
your_api_key = "YOUR_API_KEY_HERE"

# go to https://www.koinde.com/user-account/my-ads/ get your ad id number
your_ad_id = 23

# new price
price = 10000


url = "https://www.koinde.com/api/v1/update-ad"
headers = {"Content-Type": "application/json",
           "Authorization":your_api_key
}

dict = {
  "ad-id": your_ad_id,
  "price": price,
  "status": "active", # | "passive"
 }

r = requests.post(url, data=json.dumps(dict), headers=headers)

if r.status_code == 200:
    print (r.content)

#{"is_authenticated": true, "message": "Your ad is updated successfuly.", "status": "success"}
