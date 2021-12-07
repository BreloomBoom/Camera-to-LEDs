const int analogInPin = A0;
const int r = 9;
const int g = 10;
const int b = 11;

int vals[3];

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()>2) {
    for (int i = 0; i < 3; i++) {
      vals[i] = Serial.read();
    }
  }
  analogWrite(r, vals[0]);
  analogWrite(g, vals[1]);
  analogWrite(b, vals[2]);
}
