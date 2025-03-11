from flask import Flask
import subprocess
import os
import signal

app = Flask(__name__)

# Global variable to keep track of the running process
detection_process = None

@app.route('/start-detection', methods=['GET'])
def start_detection():
    global detection_process
    try:
        # Run the Python script for drowsiness detection in a separate process
        detection_process = subprocess.Popen(['python', 'ddd.py'])
        return 'Detection started!', 200
    except Exception as e:
        print(f"Error starting detection: {e}")
        return 'Failed to start detection', 500

@app.route('/stop-detection', methods=['GET'])
def stop_detection():
    global detection_process
    if detection_process:
        try:
            # Terminate the running process
            os.kill(detection_process.pid, signal.SIGTERM)
            detection_process = None
            return 'Detection stopped!', 200
        except Exception as e:
            print(f"Error stopping detection: {e}")
            return 'Failed to stop detection', 500
    else:
        return 'No active detection process to stop', 400

if __name__ == '__main__':
    app.run(debug=True)
