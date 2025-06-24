# A Hand-Gesture-Based Home Automation System

## Project Description
GestureDomotics is a smart home automation prototype that enables users to control household appliances using simple hand gestures. Leveraging computer vision and machine learning, this system translates real-time hand movements into actionable commands, providing a contactless and intuitive interface for device control.

At its core, the system consists of an ESP32 microcontroller, ESP32-CAM, and a set of output devices (LEDs and a motor) that simulate real-world appliances like lights and fans. The ESP32-CAM captures live video, which is processed using MediaPipe and OpenCV in Python to detect hand gestures. These gestures are classified using a lightweight KNN model, and corresponding commands are sent to the ESP32 via HTTP to toggle the appliances.

While this implementation uses LEDs and a small DC motor for simplicity and safety in a simulation environment, it is fully extendable to real-world home environments. By integrating relay modules, one can control actual electrical devices such as room lights, fans, or other appliances.

---

## 🏡 Real-Life Applications:
- Smart homes with touchless control
- Automation systems for elderly or disabled individuals
- Hands-free appliance control in hospitals or clean environments
- Voice-free operation in noisy or restricted areas

---

## 🚀 Features

- ✋ Real-time hand gesture detection using a webcam
- 📡 Communication between PC and ESP32 over Wi-Fi
- 💡 Control LEDs and a DC motor through gestures
- 🧠 Custom logic to detect finger positions using MediaPipe
- 🔁 Easily extendable to real-life applications using relay modules

---

## 🔧 Hardware Used

| Component            | Quantity | Description                                           |
|----------------------|----------|-------------------------------------------------------|
| ESP32 Development Board | 1        | Handles GPIO control and Wi-Fi communication          |
| LEDs (Red, Green, Blue) | 3        | Represent home appliances (bulb, tube light, etc.)    |
| DC Motor              | 1        | Simulates a ceiling fan                               |
| Resistors (220Ω)      | 3        | For limiting current to LEDs                          |
| Jumper Wires          | As needed | For connections                                       |
| Breadboard            | 1        | For prototyping                                       |


### ✅ Real-life Implementation Tip: 
Replace LEDs with actual home lights and the DC motor with a fan. Use a 4-channel relay module to safely switch AC appliances.

---

## 💻 Software Requirements

- Arduino IDE (for ESP32)
- Python 3.9 or 3.10
- OpenCV
- MediaPipe
- Requests

Install Python dependencies:

```bash
pip install opencv-python mediapipe requests
```

---

## 🧠 How It Works

- ESP32 is programmed to expose HTTP endpoints for each device (LED/motor).
- Python script reads webcam feed and detects hand landmarks using MediaPipe.
- Gesture logic identifies raised fingers and sends a command to the ESP32.
- ESP32 receives the command and toggles the corresponding GPIO pin to control the device.

---

## 🎯 Gesture to Appliance Mapping
| Gesture   | Action                          |
| --------- | ------------------------------- |
| Thumb Up  | Turn ON Red LED (Appliance 1)   |
| Index Up  | Turn ON Green LED (Appliance 2) |
| Middle Up | Turn ON Blue LED (Appliance 3)  |
| All Down  | Turn OFF all appliances         |
| Fist      | Turn ON the motor               |

---

## 🌐 ESP32 Endpoints
Example HTTP endpoints:
| /led/thumb/on | /led/thumb/off |
| /led/index/on | /led/index/off |
| /led/middle/on | /led/middle/off |

You can test them in your browser or through the Python script.

---

## 🛠 Real-Life Application
This project can be directly implemented in real homes:
- Use relay modules instead of direct GPIO-LED connection to control high-voltage appliances.
- Replace LEDs with AC lights, and the small DC motor with a ceiling fan.
- Maintain gesture control from a safe distance using only hand movements.
⚠️ Note: Proper insulation and relay ratings must be ensured while working with AC appliances.

---

## Screenshot


---

