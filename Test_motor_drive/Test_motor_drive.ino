const int rIn4 = 8;
void setup() {
  // put your setup code here, to run once:
  pinMode(rIn4, OUTPUT);
  digitalWrite(rIn4, LOW);
  Serial.begin(9600);  
}

void loop() {
  // put your main code here, to run repeatedly:
  // motor turn for 5 seconds then stall for 1 sec
    digitalWrite(rIn4, HIGH);
    delay(1000);
    digitalWrite(rIn4, LOW);
    delay(5000);
}
