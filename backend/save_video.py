import requests
import json
import time
# from bs4 import BeautifulSoup/
import re
from create_video import hosted_url, video_id
import os

url = "https://tavusapi.com/v2/videos/" + video_id

headers = {"x-api-key": "4f0cf1d227a2478a89182fde9bddf8d3"}

response = requests.request("GET", url, headers=headers)

while True:
    response = json.loads(requests.request("GET", url, headers=headers).text)
    if response["status"] == "ready":
        break
    time.sleep(2)

# Step 1: Fetch the webpage
tavus_url = hosted_url
res = requests.get(tavus_url)
res.raise_for_status()  

# Step 2: Parse the HTML
html = res.text

match = re.search(r'"download_url":"(https://[^"]+)"', html)
if match:
    download_url = match.group(1)
    print("Download URL:", download_url)
    save_folder = "../frontend/src/assets/video"
    filename = "downloaded_video.mp4"
    save_path = os.path.join(save_folder, filename)
    os.makedirs(save_folder, exist_ok=True)
    response = requests.get(download_url, stream=True)  # Stream the content for large files
    response.raise_for_status()
    with open(save_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):  # Write in chunks of 8 KB
            file.write(chunk)

    print(f"Video downloaded and saved to {save_path}.")
else:
    print("Download URL not found.")