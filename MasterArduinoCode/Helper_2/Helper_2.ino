/*

*/
const int RELAY_PIN_1 = 2;
const int RELAY_PIN_2 = 3;
const int RELAY_PIN_3 = 4;
const int RELAY_PIN_4 = 5;
const int RELAY_PIN_5 = 6;
const int RELAY_PIN_6 = 7;
const int RELAY_PIN_7 = 8;
const int RELAY_PIN_8 = 9;


void setup() {
  pinMode(RELAY_PIN_1, OUTPUT);
  pinMode(RELAY_PIN_2, OUTPUT);
  pinMode(RELAY_PIN_3, OUTPUT);
  pinMode(RELAY_PIN_4, OUTPUT);
  pinMode(RELAY_PIN_5, OUTPUT);
  pinMode(RELAY_PIN_6, OUTPUT);
  pinMode(RELAY_PIN_7, OUTPUT);
  pinMode(RELAY_PIN_8, OUTPUT);
}

void loop() {
  int sensorValue_1 = analogRead(A0);
  int sensorValue_2 = analogRead(A1);
  int sensorValue_3 = analogRead(A2);
  int sensorValue_4 = analogRead(A3);
  
  //attachment control
  if( sensorValue_1 > 500 ){
    //IDLE
    digitalWrite(RELAY_PIN_1, LOW); 
    digitalWrite(RELAY_PIN_2, LOW); 
    digitalWrite(RELAY_PIN_3, LOW);
    digitalWrite(RELAY_PIN_4, LOW); 
    digitalWrite(RELAY_PIN_5, LOW); 
    digitalWrite(RELAY_PIN_6, LOW);
    digitalWrite(RELAY_PIN_7, LOW); 
    digitalWrite(RELAY_PIN_8, LOW); 
  } else if ( sensorValue_2 > 500 ){
    //FORWARD AUGER
    digitalWrite(RELAY_PIN_1, LOW); 
    digitalWrite(RELAY_PIN_2, HIGH); 
    digitalWrite(RELAY_PIN_3, LOW);
    digitalWrite(RELAY_PIN_4, HIGH); 
  } else if ( sensorValue_3 > 500 ){
    //BACKWARDS AUGER
    digitalWrite(RELAY_PIN_1, HIGH); 
    digitalWrite(RELAY_PIN_2, LOW); 
    digitalWrite(RELAY_PIN_3, HIGH);
    digitalWrite(RELAY_PIN_4, LOW); 
  } else if ( sensorValue_4 > 500 ){
    //PUMP
    digitalWrite(RELAY_PIN_5, HIGH); 
  }
}

