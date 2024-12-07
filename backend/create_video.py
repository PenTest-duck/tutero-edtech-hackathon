import requests
import json

url = "https://tavusapi.com/v2/videos"

payload = {
    "background_url": "",
    "replica_id": "rde3b1a18f",
    "script": "Hey Fred, get back to work!",
    "video_name": "reminder"
}
headers = {
    "x-api-key": "4f0cf1d227a2478a89182fde9bddf8d3",
    "Content-Type": "application/json"
}

response = json.loads(requests.request("POST", url, json=payload, headers=headers).text)

print(response)

hosted_url = response["hosted_url"]
video_id = response["video_id"]
print(hosted_url)