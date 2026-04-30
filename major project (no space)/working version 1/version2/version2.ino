#include <WiFi.h>
#include <WebServer.h>

// Wi-Fi credentials
const char* ssid = "Clary";
const char* password = "parnika_sing";

// Web server on port 80
WebServer server(80);

// Pin definitions
#define LED_INDEX 25
#define LED_MIDDLE 26
#define LED_THUMB 27

String lastCommand = "None";

void handleCommand() {
  // Extract command from URI by removing "/cart/" (6 chars)
  String command = server.uri().substring(6);
  lastCommand = command;

  if (command == "add") {
    digitalWrite(LED_THUMB, LOW);
  } else if (command == "remove") {
    digitalWrite(LED_THUMB, HIGH);
  } else if (command == "index/on") {
    digitalWrite(LED_INDEX, LOW);
  } else if (command == "index/off") {
    digitalWrite(LED_INDEX, HIGH);
  } else if (command == "middle/on") {
    digitalWrite(LED_MIDDLE, LOW);
  } else if (command == "middle/off") {
    digitalWrite(LED_MIDDLE, HIGH);
  } else if (command == "all/down") {
    digitalWrite(LED_INDEX, HIGH);
    digitalWrite(LED_MIDDLE, HIGH);
    digitalWrite(LED_THUMB, HIGH);
  } else {
    server.send(400, "text/plain", "Invalid command: " + command);
    return;
  }

  server.send(200, "text/plain", "Command received: " + command);
}

void handleGetCommand() {
  server.send(200, "text/plain", lastCommand);
}

void setup() {
  Serial.begin(115200);

  // Set LED pins as outputs and turn them off initially
  pinMode(LED_INDEX, OUTPUT);
  pinMode(LED_MIDDLE, OUTPUT);
  pinMode(LED_THUMB, OUTPUT);
  digitalWrite(LED_INDEX, HIGH);
  digitalWrite(LED_MIDDLE, HIGH);
  digitalWrite(LED_THUMB, HIGH);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected! IP Address: " + WiFi.localIP().toString());

  // Route for handling commands under /cart/{command}
  server.on("/cart", HTTP_GET, []() {
    // If no command provided
    server.send(400, "text/plain", "No command provided");
  });
  server.on("/cart/", HTTP_GET, handleCommand); // Handle any /cart/xyz command

  // Route for sending back the last command
  server.on("/command", HTTP_GET, handleGetCommand);

  // Optional root route
  server.on("/", HTTP_GET, []() {
    server.send(200, "text/plain", "ESP32 Web Controller is running");
  });

  // Start the server
  server.begin();
  Serial.println("Server started");
}

void loop() {
  server.handleClient();
}
