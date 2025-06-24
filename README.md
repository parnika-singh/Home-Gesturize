# Hand-Gesture-Based Home Automation System using ESP32 and MediaPipe

A simplified home automation prototype that uses real-time hand gesture recognition to control electrical appliances like lights and fans. This project is built using **ESP32**, **Python**, **OpenCV**, and **MediaPipe** for gesture detection, and a simple web server to trigger appliance control via HTTP.

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

