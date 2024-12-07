import cv2
import time
from groq import Groq
from dotenv import load_dotenv, find_dotenv
import os
import torch
import numpy as np
from pathlib import Path
from torchvision.models.detection import maskrcnn_resnet50_fpn
from torchvision import transforms

model = maskrcnn_resnet50_fpn(pretrained=True)
print(model)
model.eval()  # Set the model to evaluation mode

# Define a transform to normalize the input image
transform = transforms.Compose([transforms.ToTensor()])

def detect_phone(prediction):
    phone_detected = False
    # Iterate over each detected object in the prediction
    for i in range(len(prediction[0]['labels'])):
        label = prediction[0]['labels'][i]
        confidence = prediction[0]['scores'][i].item()

        # Check if the detected object is a phone (class 67 in COCO dataset)
        if label == 1 and confidence > 0.5:  # Confidence threshold
            phone_detected = True
            break
    return phone_detected


def show_webcam():
    # Open the default webcam (0 is the default camera index)
    cap = cv2.VideoCapture(0)

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

        # Convert the frame to a tensor
        image_tensor = transform(frame)
        image_tensor = image_tensor.unsqueeze(0)  # Add batch dimension

        with torch.no_grad():
            # Get the model prediction (probabilities for each pixel)
            prediction = model(image_tensor)

        # Check if a phone is detected
        phone_detected = detect_phone(prediction)

        # Draw a bounding box or display a message if a phone is detected
        if phone_detected:
            cv2.putText(frame, "Person Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "No person Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Display the frame with the message
        cv2.imshow("Webcam Feed with Mask R-CNN", frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_webcam()