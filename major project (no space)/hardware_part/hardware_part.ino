// Pins for LEDs
#define LED_RED    25
#define LED_GREEN  26
#define LED_BLUE   27
#define motor 13

void setup() {
  // LED pins
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  pinMode(motor, OUTPUT);

  // Turn on LEDs one by one
  digitalWrite(LED_RED, HIGH);
  delay(500);
  digitalWrite(LED_GREEN, HIGH);
  delay(500);
  digitalWrite(LED_BLUE, HIGH);
  delay(500);
  digitalWrite(motor, HIGH);
}

void loop() {
  // Turn off all LEDs
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_GREEN, HIGH);
  digitalWrite(LED_BLUE, LOW);
  digitalWrite(motor, HIGH);

  delay(1000);

  // Turn on all LEDs
  digitalWrite(LED_RED, HIGH);
  digitalWrite(LED_GREEN, LOW);
  digitalWrite(LED_BLUE, HIGH);

  delay(1000);
}
