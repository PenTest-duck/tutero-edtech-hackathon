import cv2
import time
from groq import Groq


def show_webcam():
    # Open the default webcam (0 is the default camera index)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("You need to enable the webcam bro!")
        return

    print("Press 'q' to quit the webcam feed.")
    
    while True:
        # Capture frame-by-frame...
        # ret is if frame successfully captured
        # frame is the numpy array of the image frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        cv2.imshow("Webcam Feed", frame)
        time.sleep(1)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_webcam()