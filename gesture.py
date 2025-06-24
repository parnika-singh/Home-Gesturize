import cv2
import mediapipe as mp
import requests
import time

ESP32_IP = "http://192.168.75.205"  # Replace with your ESP32's IP

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Gesture tracking
previous_gesture = None
last_command_time = time.time()

def send_command(command):
    url = f"{ESP32_IP}/cart/{command}"
    try:
        response = requests.get(url, timeout=1)
        print(f"Sent: {command}, Response: {response.text}")
        return True
    except Exception as e:
        print(f"Error sending {command}: {e}")
        return False

def get_finger_state(landmarks):
    """Returns which fingers are up (True) or down (False)"""
    return {
        'thumb': landmarks[4].x < landmarks[3].x,
        'index': landmarks[8].y < landmarks[6].y,
        'middle': landmarks[12].y < landmarks[10].y,
        'ring': landmarks[16].y < landmarks[14].y,
        'pinky': landmarks[20].y < landmarks[18].y
    }

def determine_gesture(finger_state):
    """Determine which gesture is being made based on finger positions"""
    t = finger_state['thumb']
    i = finger_state['index']
    m = finger_state['middle']
    r = finger_state['ring']
    p = finger_state['pinky']

    # Check combinations in order of complexity
    if t and i and m and not (r or p):
        return "thumb+index+middle"  # All LEDs ON
    elif i and m and not (t or r or p):
        return "index+middle"       # Red + Green LEDs
    elif t and i and not (m or r or p):
        return "thumb+index"        # Yellow + Red LEDs
    elif t and m and not (i or r or p):
        return "thumb+middle"       # Yellow + Green LEDs
    elif t and not (i or m or r or p):
        return "thumb"              # Yellow LED
    elif i and not (t or m or r or p):
        return "index"              # Red LED
    elif m and not (t or i or r or p):
        return "middle"             # Green LED
    elif all([t, i, m, r, p]):
        return "open"               # Motor ON
    elif not any([t, i, m, r, p]):
        return "fist"               # All OFF
    return None

def process_frame(frame):
    global previous_gesture, last_command_time
    
    # Flip and convert the frame
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process with MediaPipe
    results = hands.process(rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get finger states and determine gesture
            finger_state = get_finger_state(hand_landmarks.landmark)
            current_gesture = determine_gesture(finger_state)
            
            # Only send new commands with 0.5s cooldown
            if current_gesture and current_gesture != previous_gesture:
                if time.time() - last_command_time > 0.5:  # Anti-spam delay
                    if send_command(current_gesture):
                        previous_gesture = current_gesture
                        last_command_time = time.time()
    
    # Display status
    status = f"Last Gesture: {previous_gesture}" if previous_gesture else "No gesture"
    cv2.putText(frame, status, (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    return frame

def main():
    cap = cv2.VideoCapture(0)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        processed_frame = process_frame(frame)
        cv2.imshow('Gesture Control', processed_frame)
        
        if cv2.waitKey(5) & 0xFF == 27:  # ESC to exit
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()