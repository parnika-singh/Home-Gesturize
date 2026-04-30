import cv2
import mediapipe as mp
import requests

# ===== Replace this with your ESP32 IP address =====
ESP32_IP = "http://192.168.75.186"  # Example: "http://192.168.1.24"

# ===== Initialize MediaPipe Hands =====
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# ===== Function to send hand gesture commands to ESP32 =====
def control_led(endpoint):
    url = f"{ESP32_IP}/cart/{endpoint}"
    try:
        response = requests.get(url, timeout=1)
        print(f"Sent command: {endpoint}, ESP32 Response: {response.text}")
    except Exception as e:
        print(f"Failed to send command: {endpoint}, Error: {e}")

# ===== Function to fetch commands from ESP32 =====
def fetch_esp32_command():
    try:
        url = f"{ESP32_IP}/command"
        response = requests.get(url, timeout=1)
        return response.text.strip()
    except Exception as e:
        print(f"Error fetching command from ESP32: {e}")
        return None

# ===== Function to detect the state of each finger =====
def count_fingers(hand_landmarks):
    landmarks = hand_landmarks.landmark

    # Finger logic (based on MediaPipe landmarks)
    thumb_up = landmarks[mp_hands.HandLandmark.THUMB_TIP].x < landmarks[mp_hands.HandLandmark.THUMB_IP].x
    index_up = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_up = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_up = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_up = landmarks[mp_hands.HandLandmark.PINKY_TIP].y < landmarks[mp_hands.HandLandmark.PINKY_PIP].y

    # Finger states
    finger_status = [thumb_up, index_up, middle_up, ring_up, pinky_up]

    # Send corresponding commands to ESP32
    control_led("add" if thumb_up else "remove")
    control_led("index/on" if index_up else "index/off")
    control_led("middle/on" if middle_up else "middle/off")

    # Optional: handle all fingers down
    if not any(finger_status):
        print("All fingers are down")
        control_led("all/down")

    return finger_status

# ===== Initialize Webcam =====
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand landmarks
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            count_fingers(hand_landmarks)

    # Display fetched command from ESP32
    esp32_command = fetch_esp32_command()
    if esp32_command:
        cv2.putText(frame, f"ESP32 Command: {esp32_command}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow('Hand Gesture Recognition', frame)

    # Exit on ESC key
    if cv2.waitKey(5) & 0xFF == 27:
        break

# ===== Cleanup =====
cap.release()
cv2.destroyAllWindows()
