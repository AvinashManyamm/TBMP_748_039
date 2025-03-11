from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# Global variable to store the detection process
detection_process = None

@app.route('/start-detection', methods=['GET'])
def start_detection():
    global detection_process
    if detection_process is None:
        try:
            # Start the ddd.py script using subprocess
            detection_process = subprocess.Popen(['python', 'ddd.py'])  # Adjust this command to point to your script
            return jsonify(message="Detection started successfully!")
        except Exception as e:
            return jsonify(message=f"Failed to start detection: {str(e)}"), 500
    else:
        return jsonify(message="Detection is already running."), 400

@app.route('/stop-detection', methods=['GET'])
def stop_detection():
    global detection_process
    if detection_process is not None:
        try:
            # Gracefully terminate the running process
            detection_process.terminate()  
            detection_process = None
            return jsonify(message="Detection stopped successfully!")
        except Exception as e:
            return jsonify(message=f"Failed to stop detection: {str(e)}"), 500
    else:
        return jsonify(message="No detection is running."), 400

if __name__ == '__main__':
    app.run(debug=True)
