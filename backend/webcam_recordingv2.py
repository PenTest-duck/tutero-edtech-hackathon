import cv2
import tensorflow as tf
import numpy as np
import json
import urllib.request
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
import sys
import os

# Terrible code that was not refined

# Load ImageNet class labels
url = "https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json"
with urllib.request.urlopen(url) as f:
    class_idx = json.load(f)
class_labels = {v[0]: v[1] for v in class_idx.values()}

# Load pre-trained ResNet50 model from TensorFlow Keras
model = ResNet50(weights='imagenet')

def softmax(logits):
    exp_logits = np.exp(logits - np.max(logits))  # Subtract max for numerical stability
    return exp_logits / np.sum(exp_logits)

def detect_objects(frame):
    pil_image = image.array_to_img(frame)

    # (224, 224) for ResNet input
    pil_image = pil_image.resize((224, 224))

    img_array = image.img_to_array(pil_image)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess for ResNet50

    # print("THE IMAGE SHAPE IS", img_array.shape)

    # Quiet the terminal to not display estimation time for each frame
    sys.stdout = open(os.devnull, 'w')
    predictions = model(img_array)
    sys.stdout = sys.__stdout__

    probabilities = softmax(predictions)

    # Get the predicted class of the top 5 (I know its slow)
    predicted_class = np.argmax(probabilities)
    new_array = np.delete(probabilities, predicted_class)
    predicted_class2 = np.argmax(new_array)
    new_array2 = np.delete(new_array, predicted_class2)
    predicted_class3 = np.argmax(new_array2)
    new_array3 = np.delete(new_array, predicted_class3)
    predicted_class4 = np.argmax(new_array3)
    new_array4 = np.delete(new_array, predicted_class4)
    predicted_class5 = np.argmax(new_array4)

    # print("THESE ARE THE PREDICTIONS", predicted_class)

    return predicted_class, predicted_class2, predicted_class3, predicted_class4, predicted_class5

def show_webcam():
    counter = 0
    # Open the default webcam (0 is the default camera index)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("You need to enable the webcam bro!")
        return

    print("Press 'q' to quit the webcam feed.")

    while True:
        # Ret is boolean, frame is an image
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Detect five most prominent
        first, second, third, fourth, fifth = detect_objects(frame)

        phone_keywords = [
            "cellular telephone", "cellular phone", "cellphone", "cell", "mobile phone"
        ]

        # The imageNet classes that we want
        correct_nums = [
            761, 487, 707, 650
        ]

        if (
            first in correct_nums
        ):
            counter += 1
            print(counter, "YES THERE IS A PHONE IN THIS", first)
        if (
            second in correct_nums
        ):
            counter += 1
            print(counter, "YES THERE IS A PHONE IN THIS", second)
        if (
            third in correct_nums
        ):
            counter += 1
            print(counter, "YES THERE IS A PHONE IN THIS", third)
        if (
            fourth in correct_nums
        ):
            counter += 1
            print(counter, "YES THERE IS A PHONE IN THIS", first)
        if (
            fifth in correct_nums
        ):
            counter += 1
            print(counter, "YES THERE IS A PHONE IN THIS", first)

        cv2.imshow("Webcam Feed with ResNet50", frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_webcam()
