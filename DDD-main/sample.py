import cv2

cap = cv2.VideoCapture(0)  # Using the default webcam (0)
if not cap.isOpened():
    print("Error: Could not access the camera")
else:
    print("Successfully opened the camera")

cap.release()
