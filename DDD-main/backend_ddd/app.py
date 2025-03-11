import cv2
from flask import Flask, jsonify, Response, request
from flask_cors import CORS
import threading

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Global variables
video_cap = None
detection_active = False
input_source = "http://192.168.0.211:4747/video"  # Default to DroidCam IP

# Function to start video capture
def start_video_feed(input_source):
    global video_cap
    video_cap = cv2.VideoCapture(input_source)  # Use FFMPEG as backend
    if not video_cap.isOpened():
        print(f"Failed to open video feed from source: {input_source}.")
        return False
    else:
        print(f"Video feed started successfully from source: {input_source}.")
        return True

# Route to set input source
@app.route('/set-input-source', methods=['POST'])
def set_input_source():
    global input_source, video_cap
    data = request.json
    new_source = data.get("source", input_source)
    
    # Release current video capture if active
    if video_cap is not None and video_cap.isOpened():
        video_cap.release()

    # Attempt to start new video feed
    if start_video_feed(new_source):
        input_source = new_source
        return jsonify({"message": f"Input source set to {new_source}"}), 200
    else:
        return jsonify({"message": "Failed to start video feed from the new source"}), 400

# Route to start detection
@app.route('/start-detection', methods=['GET'])
def start_detection():
    global detection_active
    detection_active = True
    return jsonify({"message": "Drowsiness detection started"}), 200

# Route to stop detection
@app.route('/stop-detection', methods=['GET'])
def stop_detection():
    global detection_active
    detection_active = False
    return jsonify({"message": "Drowsiness detection stopped"}), 200

# Route for SOS alert
@app.route('/sos-alert', methods=['POST'])
def sos_alert():
    data = request.json
    message = data.get("message", "SOS Alert triggered!")
    print(f"SOS Alert: {message}")
    return jsonify({"message": "SOS Alert received"}), 200

# Route to stream video feed
@app.route('/video_feed')
def video_feed():
    def generate():
        while True:
            if video_cap is None or not video_cap.isOpened():
                break

            success, frame = video_cap.read()
            if not success:
                break

            # Send raw frame in response
            ret, jpeg = cv2.imencode('.jpg', frame)
            if not ret:
                break

            # Yield frame as JPEG image for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Run the video processing in a separate thread
def video_processing():
    global detection_active, video_cap
    while True:
        if not detection_active or video_cap is None or not video_cap.isOpened():
            continue

        success, frame = video_cap.read()
        if not success:
            print("Failed to retrieve video feed.")
            break

        # Process the frame for drowsiness detection (add logic here)
        cv2.imshow('Drowsiness Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if video_cap and video_cap.isOpened():
        video_cap.release()
    cv2.destroyAllWindows()

# Run the video processing in a separate thread
threading.Thread(target=video_processing, daemon=True).start()

if __name__ == '__main__':
    start_video_feed(input_source)
    app.run(debug=True, host='0.0.0.0', port=5000)
