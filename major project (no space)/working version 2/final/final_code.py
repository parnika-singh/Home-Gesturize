import cv2
import mediapipe as mp
import requests

ESP32_IP = "http://192.168.75.205"  # Replace with your ESP32's IP

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

previous_state = None

def send_command(command):
    url = f"{ESP32_IP}/cart/{command}"
    try:
        response = requests.get(url, timeout=1)
        print(f"Sent: {command}, ESP32 replied: {response.text}")
    except Exception as e:
        print(f"Error sending command {command}: {e}")

def fetch_last_command():
    try:
        response = requests.get(f"{ESP32_IP}/command", timeout=1)
        return response.text.strip()
    except:
        return "No ESP32 response"

def detect_gesture(hand_landmarks):
    global previous_state
    lm = hand_landmarks.landmark

    thumb_up = lm[4].x < lm[3].x
    index_up = lm[8].y < lm[6].y
    middle_up = lm[12].y < lm[10].y
    ring_up = lm[16].y < lm[14].y
    pinky_up = lm[20].y < lm[18].y

    gesture = (thumb_up, index_up, middle_up, ring_up, pinky_up)

    if gesture == previous_state:
        return
    previous_state = gesture

    if all(gesture):
        send_command("open")   # Open palm
    elif not any(gesture):
        send_command("fist")   # Fist
    elif thumb_up and not any(gesture[1:]):
        send_command("thumb") # Only thumb
    elif index_up and not any([thumb_up, middle_up, ring_up, pinky_up]):
        send_command("index") # Only index
    elif middle_up and not any([thumb_up, index_up, ring_up, pinky_up]):
        send_command("middle") # Only middle

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            detect_gesture(hand_landmarks)

    # Show last ESP32 command
    cmd = fetch_last_command()
    cv2.putText(frame, f"ESP32 Command: {cmd}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("ESP32 Gesture Control", frame)

    if cv2.waitKey(5) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
