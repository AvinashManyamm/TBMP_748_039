import cv2
import numpy as np
from scipy.spatial import distance
import face_recognition
import collections
from playsound import playsound
import threading
import pygame

# Function to calculate eye aspect ratio (EAR)
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Function to calculate mouth aspect ratio (MAR)
def mouth_aspect_ratio(mouth):
    A = distance.euclidean(mouth[2], mouth[10])
    B = distance.euclidean(mouth[4], mouth[8])
    C = distance.euclidean(mouth[0], mouth[6])
    mar = (A + B) / (2.0 * C)
    return mar

# Function to process the frame and detect drowsiness or yawning
def process_image(frame):
    # Define thresholds
    EYE_AR_THRESH = 0.2  # Lower to make detection more sensitive
    MOUTH_AR_THRESH = 0.5  # Adjust for yawning sensitivity

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all face locations
    face_locations = face_recognition.face_locations(rgb_frame)

    eye_flag = mouth_flag = False
    ear = mar = 0.0  # Initialize EAR and MAR to default values

    if face_locations:
        for face_location in face_locations:
            # Extract facial landmarks
            landmarks = face_recognition.face_landmarks(rgb_frame, [face_location])[0]
            # Extract eye and mouth coordinates
            left_eye = np.array(landmarks['left_eye'])
            right_eye = np.array(landmarks['right_eye'])
            mouth = np.array(landmarks['bottom_lip'])

            # Calculate EAR and MAR
            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2.0
            mar = mouth_aspect_ratio(mouth)

            # Check if eyes are closed
            if ear < EYE_AR_THRESH:
                eye_flag = True

            # Check if yawning
            if mar > MOUTH_AR_THRESH:
                mouth_flag = True

    return ear, mar, eye_flag, mouth_flag

# Function to play the alert sound
def play_alert():
    pygame.mixer.init()  # Initialize the mixer module
    while True:
        if playing_alert[0]:
            pygame.mixer.music.load("alert.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():  # Wait until the sound finishes
                pygame.time.Clock().tick(10)
        else:
            break

# Start capturing video from IP camera
video_cap = cv2.VideoCapture("http://10.0.0.3:4747/video")
count = score = 0

# Moving average deques to smooth display
ear_values = collections.deque(maxlen=10)
mar_values = collections.deque(maxlen=10)
scores = collections.deque(maxlen=10)

# Shared variable to manage audio alert
playing_alert = [False]

while True:
    success, image = video_cap.read()
    if not success:
        print("Failed to retrieve video feed. Check the IP address and connectivity.")
        break

    image = cv2.resize(image, (800, 500))

    count += 1
    n = 15  # Process every nth frame
    if count % n == 0:
        # Process the frame
        ear_value, mar_value, eye_flag, mouth_flag = process_image(image)

        # Update moving average deque
        ear_values.append(ear_value)
        mar_values.append(mar_value)

        # Update score
        if eye_flag or mouth_flag:
            score += 1  # Increment score if eyes are closed or yawning is detected
        else:
            score -= 2  # Aggressively reduce score if no drowsiness is detected
            if score < 0:
                score = 0  # Ensure score doesn't go negative
        scores.append(score)

    # Ensure mouth_flag has a default value for non-processed frames
    if 'mouth_flag' not in locals():
        mouth_flag = False

    # Compute stabilized values
    stabilized_ear = sum(ear_values) / len(ear_values) if ear_values else 0.0
    stabilized_mar = sum(mar_values) / len(mar_values) if mar_values else 0.0
    stabilized_score = round(sum(scores) / len(scores)) if scores else 0

    # Manage audio alert based on score
    if stabilized_score >= 5 and not playing_alert[0]:
        playing_alert[0] = True
        threading.Thread(target=play_alert, daemon=True).start()
    elif stabilized_score < 5 and playing_alert[0]:
        playing_alert[0] = False

    # Display EAR and MAR values
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, f"EAR: {stabilized_ear:.2f}", (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(image, f"MAR: {stabilized_mar:.2f}", (10, 60), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display score
    # First, display the "Score" label in one color (e.g., dark red)
    cv2.putText(image, "Score:", (10, image.shape[0] - 10), font, 1, (139, 0, 0), 2, cv2.LINE_AA)

    # Then, display the actual stabilized score in a different color (e.g., green)
    cv2.putText(image, f"{stabilized_score}", (120, image.shape[0] - 10), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display alerts
    if stabilized_score >= 5:
        cv2.putText(image, "Drowsy!", (image.shape[1] - 130, 40), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    if mouth_flag and stabilized_mar > 0.5:  # Add explicit yawning prompt
        cv2.putText(image, "Yawning", (image.shape[1] - 130, 80), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Show the frame
    cv2.imshow('Drowsiness Detection', image)

    # Exit loop on key press
    if cv2.waitKey(1) & 0xFF != 255:
        break

video_cap.release()
cv2.destroyAllWindows()
