const int SWITCH = 2;

void setup() { 
  pinMode(SWITCH, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(SWITCH) == HIGH) {
    Serial.print("1\n");
  } else {
    Serial.print("0\n");
  }
  delay(500);
}
