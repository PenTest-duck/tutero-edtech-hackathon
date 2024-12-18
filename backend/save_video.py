import requests
import json
import time
# from bs4 import BeautifulSoup/
import re
from create_video import create_video
import os
import env

def save_video2(transcript):
    [video_id, hosted_url] = create_video(transcript)
    headers = {"x-api-key": env.TAVUS_API_KEY}
    url = "https://tavusapi.com/v2/videos/" + video_id
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
        save_folder = "../frontend/public"
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

# save_video2("keep going Freddie, your future self will thank you. we're having so much fun at this hackathon today")
