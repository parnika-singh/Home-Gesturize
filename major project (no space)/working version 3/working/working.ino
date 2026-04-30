#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "Clary";
const char* password = "parnika_sing";

WebServer server(80);

// LED and Motor Pins
#define YELLOW_LED_1  26
#define YELLOW_LED_2  32
#define RED_LED_1     14
#define RED_LED_2     25
#define GREEN_LED_1   27
#define GREEN_LED_2   33
#define MOTOR_PIN     12

String lastCommand = "none";

void resetAll() {
  digitalWrite(YELLOW_LED_1, HIGH);
  digitalWrite(YELLOW_LED_2, HIGH);
  digitalWrite(RED_LED_1, HIGH);
  digitalWrite(RED_LED_2, HIGH);
  digitalWrite(GREEN_LED_1, HIGH);
  digitalWrite(GREEN_LED_2, HIGH);
  digitalWrite(MOTOR_PIN, LOW);
  Serial.println("All outputs OFF");
}

void handleRoot() {
  server.send(200, "text/plain", "ESP32 Gesture Control Server");
}

void handleCart() {
  String command = server.uri().substring(6); // Extract command from "/cart/..."
  lastCommand = command;
  Serial.println("Received: " + command);

  resetAll(); // Reset all outputs first

  // Single Gestures
  if (command == "thumb") {
    digitalWrite(YELLOW_LED_1, LOW);
    digitalWrite(YELLOW_LED_2, LOW);
  }
  else if (command == "index") {
    digitalWrite(RED_LED_1, LOW);
    digitalWrite(RED_LED_2, LOW);
  }
  else if (command == "middle") {
    digitalWrite(GREEN_LED_1, LOW);
    digitalWrite(GREEN_LED_2, LOW);
  }
  else if (command == "open") {
    digitalWrite(MOTOR_PIN, HIGH);
  }
  else if (command == "fist") {
    // Already handled by resetAll()
  }

  // Combined Gestures
  else if (command == "thumb+index") {
    digitalWrite(YELLOW_LED_1, LOW);
    digitalWrite(YELLOW_LED_2, LOW);
    digitalWrite(RED_LED_1, LOW);
    digitalWrite(RED_LED_2, LOW);
  }
  else if (command == "thumb+middle") {
    digitalWrite(YELLOW_LED_1, LOW);
    digitalWrite(YELLOW_LED_2, LOW);
    digitalWrite(GREEN_LED_1, LOW);
    digitalWrite(GREEN_LED_2, LOW);
  }
  else if (command == "index+middle") {
    digitalWrite(RED_LED_1, LOW);
    digitalWrite(RED_LED_2, LOW);
    digitalWrite(GREEN_LED_1, LOW);
    digitalWrite(GREEN_LED_2, LOW);
  }
  else if (command == "thumb+index+middle") {
    digitalWrite(YELLOW_LED_1, LOW);
    digitalWrite(YELLOW_LED_2, LOW);
    digitalWrite(RED_LED_1, LOW);
    digitalWrite(RED_LED_2, LOW);
    digitalWrite(GREEN_LED_1, LOW);
    digitalWrite(GREEN_LED_2, LOW);
  }
  else {
    server.send(404, "text/plain", "Invalid command");
    return;
  }

  server.send(200, "text/plain", "OK: " + command);
}

// ADD THIS MISSING FUNCTION
void handleGetCommand() {
  server.send(200, "text/plain", lastCommand);
}

void setup() {
  Serial.begin(115200);

  // Initialize outputs
  pinMode(YELLOW_LED_1, OUTPUT);
  pinMode(YELLOW_LED_2, OUTPUT);
  pinMode(RED_LED_1, OUTPUT);
  pinMode(RED_LED_2, OUTPUT);
  pinMode(GREEN_LED_1, OUTPUT);
  pinMode(GREEN_LED_2, OUTPUT);
  pinMode(MOTOR_PIN, OUTPUT);
  resetAll();

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) delay(500);
  Serial.println("\nConnected! IP: " + WiFi.localIP().toString());

  // Set up server routes
  server.on("/", handleRoot);
  server.on("/cart/thumb", handleCart);
  server.on("/cart/index", handleCart);
  server.on("/cart/middle", handleCart);
  server.on("/cart/open", handleCart);
  server.on("/cart/fist", handleCart);
  server.on("/cart/thumb+index", handleCart);
  server.on("/cart/thumb+middle", handleCart);
  server.on("/cart/index+middle", handleCart);
  server.on("/cart/thumb+index+middle", handleCart);
  server.on("/command", handleGetCommand);  // Now properly defined

  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}