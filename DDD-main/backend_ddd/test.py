import cv2

stream_url = "http://192.168.0.211:4747/video"

cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print(f"Failed to open video feed from source: {stream_url}")
else:
    print(f"Successfully opened video feed from source: {stream_url}")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame from video stream")
        break
    cv2.imshow("Stream Test", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
