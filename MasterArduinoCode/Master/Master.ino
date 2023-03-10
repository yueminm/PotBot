/*
Master Arduino, will control the other two
*/

void setup() {
  pinMode(2, OUTPUT);    // idle motion
  pinMode(3, OUTPUT);    // right
  pinMode(4, OUTPUT);    // left
  pinMode(5, OUTPUT);    // Forward
  pinMode(6, OUTPUT);    // BACKWARDS
  pinMode(7, OUTPUT);    // idle attachments
  pinMode(8, OUTPUT);    // forwards auger
  pinMode(9, OUTPUT);    // backwards auger
  pinMode(10, OUTPUT);   // pump
}

void loop() {
  //something here has to determine how we are going to communicate what we need done and what should be put on
  int movement_angle = 
  int forward = 
  int volume = 
  boolean water = // to know if we are watering
  boolean asphalt = // to know if we are poaring asphalt
  
  
  
  //ASSUMING ALL VARIABLES ABOVE ARE CORRECTLY DETERMINED
  int interval = (int) (movement_angle / 20) *1000 // (theta/(D sec/D theta)) * (1000 millisec / sec)
  int interval_forward = forward *1000 // we can change this as we go
  int interval_asphalt = volume * 1000 //we can change this as we know how much the robot puts out
  if (water == false){
    if (movement_angle == 0){
      //Forward
      digitalWrite(5,HIGH) 
      delay(interval_forward)
      digitalWrite(5,LOW)
    } if else (movement_angle > 0){
      //Right turn
      digitalWrite(3,HIGH) 
      delay(interval)
      digitalWrite(3,LOW)
    } if else (movement_angle < 0){
      //Left turn
      digitalWrite(4,HIGH) 
      delay(interval)
      digitalWrite(4,LOW)
    }
  }
  
  if (water == true){
      //Forward and spray water
      digitalWrite(5,HIGH) 
      digitalWrite(10,HIGH)
      delay(interval_forward)
      digitalWrite(5,LOW)
      digitalWrite(10,LOW)
  }
  
  if (asphalt == true){
      //Forward and spray water
      digitalWrite(8,HIGH) 
      delay(interval_asphalt)
      digitalWrite(8,LOW)
  }
  
  
}
