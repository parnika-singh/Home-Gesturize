// Pin definitions
#define RED_LED_1     14
#define RED_LED_2     25
#define YELLOW_LED_1  26
#define YELLOW_LED_2  32
#define GREEN_LED_1   27
#define GREEN_LED_2   33
#define MOTOR_PIN     12

void setup() {
  // Start Serial for debugging
  Serial.begin(115200);
  Serial.println("Turning ON all LEDs and Motor (active LOW)");

  // Set pins as OUTPUT
  pinMode(RED_LED_1, OUTPUT);
  pinMode(RED_LED_2, OUTPUT);
  pinMode(YELLOW_LED_1, OUTPUT);
  pinMode(YELLOW_LED_2, OUTPUT);
  pinMode(GREEN_LED_1, OUTPUT);
  pinMode(GREEN_LED_2, OUTPUT);
  pinMode(MOTOR_PIN, OUTPUT);

  // Turn ON all devices (LOW = ON)
  digitalWrite(RED_LED_1, LOW);
  digitalWrite(RED_LED_2, LOW);
  digitalWrite(YELLOW_LED_1, LOW);
  digitalWrite(YELLOW_LED_2, LOW);
  digitalWrite(GREEN_LED_1, LOW);
  digitalWrite(GREEN_LED_2, LOW);
  digitalWrite(MOTOR_PIN, HIGH);
}

void loop() {
  // Nothing to do in loop since everything is always ON
}
