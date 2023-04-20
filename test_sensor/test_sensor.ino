/*
  Ultrasonic Sensor HC-SR04 and Arduino Tutorial

  by Dejan Nedelkovski,
  www.HowToMechatronics.com

*/
// defines pins numbers
const int trigPin = 3;
const int echoPin = 2;
// defines variables
long duration;
float distance = 0;
float measureD = 0;
float alpha = 0.5;


void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
}

unsigned long startTime = millis();

void loop()
{
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  pinMode(echoPin, INPUT); 
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  measureD = duration * 0.0343 / 2;
  // distance = alpha*measureD + (1-alpha)*distance;
  // Prints the distance on the Serial Monitor
  //Serial.print("Distance: ");
  Serial.println(measureD);
}

void outerLoop()
{
  if (millis() - startTime <= 4000)
  {
    startTime = millis();
    loop();
  }
}
