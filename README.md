# Major-Project
## Project Concept: AI-Powered Smart Car for Gesture & Voice-Controlled Wheelchair
This project involves building a toy car prototype that can be controlled using hand gestures, voice commands, or autonomous navigation, demonstrating its potential for smart wheelchairs.

### Key Features & Technologies:
- Hand Gesture Control:
Uses ESP32-CAM + OpenCV + Mediapipe to recognize hand gestures.
Different gestures (e.g., forward, backward, stop) control the car's movement.
- Voice-Controlled Navigation:
Uses ESP32 + Google Speech-to-Text API or Edge AI (Vosk, Picovoice).
Recognizes voice commands like "Move forward," "Turn left," etc.
- Obstacle Avoidance & Safety Mechanism:
Uses Ultrasonic Sensors / LiDAR to detect obstacles and stop automatically.
Can integrate AI-based object detection (YOLO) for recognizing humans/objects.
- IoT-Based Remote Control:
Connects with a mobile app or web dashboard (Firebase, MQTT, Blynk) for remote control.
- Self-Navigation Mode:
Uses Reinforcement Learning (Q-learning, Deep Q-Networks) for autonomous movement.
Can follow a pre-defined path using color detection (line following).
### Future Expansion into a Wheelchair:
The same technology can be scaled up for real wheelchairs with motorized movement and smart safety features.
Can add fall detection, emergency alerts, and AI-based obstacle recognition.

----------------------------------------------------------------------------------------------------------------------------------
## 🚗 Architecture Overview
The system consists of ESP32 for control, computer vision for gesture recognition, and voice commands for movement.

### 🔹 System Workflow:
- Input: Gesture & Voice Commands
Camera captures hand gestures → ESP32 processes via OpenCV + Mediapipe.
Microphone captures voice → Converted into text using Edge AI Speech Recognition.
- Processing & Decision Making
ESP32 receives gesture/voice input, processes commands, and sends signals to motor drivers.
If no input is given, the system enters autonomous mode and follows a predefined path or avoids obstacles.
- Output: Car Movement & Obstacle Detection
Motor drivers control the wheels based on input.
Ultrasonic sensors detect obstacles → ESP32 automatically stops or reroutes.
### 🛠️ Component List:
- 1️⃣ Microcontroller & Processing Unit
ESP32-CAM → For gesture recognition & image processing.
ESP32 DevKit V1 → Main control board for motor and sensor processing.
- 2️⃣ Input Components
OV2640 Camera Module → Captures hand gestures.
MEMS Microphone (INMP441) → Captures voice commands.
Ultrasonic Sensors (HC-SR04) → Detects obstacles.
IR Sensors (Optional) → For line-following capability.
- 3️⃣ Output Components
L298N Motor Driver → Controls DC motors.
Two DC Motors → Moves the toy car.
OLED Display (Optional) → Displays detected gestures/commands.
- 4️⃣ Power & Connectivity
Li-ion Battery (7.4V 18650) → Powers the entire system.
WiFi/Bluetooth Module (Built-in ESP32) → For IoT connectivity (Firebase/MQTT).
### 📡 Features & Functionality
- ✅ Gesture-Controlled Mode:
Recognizes 5-6 hand gestures to move forward, left, right, stop, etc.
Uses Mediapipe Hand Tracking + ESP32-CAM for real-time control.
- ✅ Voice-Controlled Mode:
Uses speech-to-text conversion for command execution.
Works offline using Vosk/Picovoice AI models.
- ✅ Obstacle Avoidance Mode:
Ultrasonic sensors detect objects within 10-15 cm range.
Car stops or auto-navigates around obstacles.
- ✅ Self-Navigation Mode (Future Upgrade)
Uses Reinforcement Learning (Q-learning/DQN) to follow a pre-defined path.
Line following (IR sensors) or GPS tracking (for real wheelchair).



