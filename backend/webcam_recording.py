import cv2
import time
from groq import Groq
from dotenv import load_dotenv
import os
import torch
import numpy as np
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
import json
import base64
import threading
import os
import requests

from save_video import save_video2

load_dotenv()
headers = {
   'Authorization': os.environ.get("BLAND_API_KEY"),
}
data = {
  "phone_number": os.environ.get("PHONE_NUMBER"),
  "from": None,
  "task": "You're Study Buddy, a study assistant. You notice a student using their phone when they should be studying. Write a message to remind them to stay focused. You should begin with the following words: ",
  "model": "enhanced",
  "language": "en",
  "voice": "nat",
  "voice_settings": {},
  "pathway_id": None,
  "local_dialing": False,
  "max_duration": 12,
  "answered_by_enabled": False,
  "wait_for_greeting": False,
  "record": False,
  "amd": False,
  "interruption_threshold": 100,
  "voicemail_message": None,
  "temperature": None,
  "transfer_phone_number": None,
  "transfer_list": {},
  "metadata": None,
  "pronunciation_guide": [],
  "start_time": None,
  "background_track": "none",
  "request_data": {},
  "tools": [],
  "dynamic_data": [],
  "analysis_preset": None,
  "analysis_schema": {},
  "webhook": None,
  "calendly": {},
  "timezone": "America/Los_Angeles"
}

TIME_INTERVAL = 10
client = Groq()

def send_to_groq(image: bytes):
    base64_image = base64.b64encode(image).decode("utf-8")

    completion = client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """
                            Check whether there is a mobile phone within this photo.
                            Also provide a description, with the first sentence being what you can see in the photo, and the second being what clothes the person in the photo is wearing.

                            Your result should be in JSON, e.g. {"contains_phone": true, "description": "A person who is using a laptop while holding a phone."}
                        """
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    }
                ]
            },
        ],
        temperature=0.1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )

    response_json = json.loads(completion.choices[0].message.content)
    contains_phone = response_json.get("contains_phone", False)

    print(f"Contains phone: {contains_phone}")
    if not contains_phone:
        return

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""
                            Description of the scenario: {response_json.get("description", "")}

                            You have just found out that a student has been using his phone when he is supposed to be studying.
                            Write a message to the student to remind him to stay focused, calling the person out by the clothes they are wearing.
                            It should be a message that can be read out in 5 seconds.

                            Return it in JSON format, e.g. "message": "Hey, guy in the white shirt, put your phone away and focus on your studies!"
                        """
                    },
                ]
            },
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )

    response_json = json.loads(completion.choices[0].message.content)
    message = response_json.get("message", "")
    print(f"{message=}")

    # save_video2(message)

    data["task"] += message
    requests.post('https://api.bland.ai/v1/calls', json=data, headers=headers)


def show_webcam():
    # Open the default webcam (0 is the default camera index)
    cap = cv2.VideoCapture(0)
    timestamp = int(time.time())
    groq_enabled = False

    if not cap.isOpened():
        print("You need to enable the webcam bro!")
        return

    print("Press 'q' to quit the webcam feed.")
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the frame with the message
        cv2.imshow("Webcam Feed with Mask R-CNN", frame)

        current = int(time.time())
        if groq_enabled and current - timestamp > TIME_INTERVAL:
            timestamp = current
            img_encode = cv2.imencode('.png', frame)[1] 
            data_encode = np.array(img_encode) 
            byte_encode = data_encode.tobytes() 

            print("Sending to Groq...")
            threading.Thread(target=send_to_groq, args=(byte_encode,)).start()

        if cv2.waitKey(1) & 0xFF == ord('g'):
            groq_enabled = not groq_enabled
            print(f"{groq_enabled=}")

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_webcam()