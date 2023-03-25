/*
  wheel testing
*/

#include "Keyboard.h"

const int front_left_1 = 2;
const int front_left_2 = 3;
const int rear_left_1 = 4;
const int rear_left_2 = 5;
const int front_right_1 = 6;
const int front_right_2 = 7;
const int rear_right_1 = 8;
const int rear_right_2 = 9;

void setup() {
  pinMode(front_left_1, OUTPUT);
  pinMode(front_left_2, OUTPUT);
  pinMode(rear_left_1, OUTPUT);
  pinMode(rear_left_2, OUTPUT);
  pinMode(front_right_1, OUTPUT);
  pinMode(front_right_2, OUTPUT);
  pinMode(rear_right_1, OUTPUT);
  pinMode(rear_right_2, OUTPUT);
  Serial.begin(9600);
  Keyboard.begin();
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    // Forward
    if (cmd == 'w') {
      digitalWrite(front_left_1, HIGH);
      digitalWrite(front_left_2, LOW);
      digitalWrite(rear_left_1, HIGH);
      digitalWrite(rear_left_2, LOW);
      digitalWrite(front_right_1, HIGH);
      digitalWrite(front_right_2, LOW);
      digitalWrite(rear_right_1, HIGH);
      digitalWrite(rear_right_2, LOW);
    }

    // Backward
    else if (cmd == 's') {
      digitalWrite(front_left_1, LOW);
      digitalWrite(front_left_2, HIGH);
      digitalWrite(rear_left_1, LOW);
      digitalWrite(rear_left_2, HIGH);
      digitalWrite(front_right_1, LOW);
      digitalWrite(front_right_2, HIGH);
      digitalWrite(rear_right_1, LOW);
      digitalWrite(rear_right_2, HIGH);
    }
    
    // Left
    else if (cmd == 'a') {
      digitalWrite(front_left_1, LOW);
      digitalWrite(front_left_2, HIGH);
      digitalWrite(rear_left_1, LOW);
      digitalWrite(rear_left_2, HIGH);
      digitalWrite(front_right_1, HIGH);
      digitalWrite(front_right_2, LOW);
      digitalWrite(rear_right_1, HIGH);
      digitalWrite(rear_right_2, LOW);
    }

    // Right
    else if (cmd == 's') {
      digitalWrite(front_left_1, HIGH);
      digitalWrite(front_left_2, LOW);
      digitalWrite(rear_left_1, HIGH);
      digitalWrite(rear_left_2, LOW);
      digitalWrite(front_right_1, LOW);
      digitalWrite(front_right_2, HIGH);
      digitalWrite(rear_right_1, LOW);
      digitalWrite(rear_right_2, HIGH);
    }
  }

  else {
    digitalWrite(front_left_1, LOW);
      digitalWrite(front_left_2, LOW);
      digitalWrite(rear_left_1, LOW);
      digitalWrite(rear_left_2, LOW);
      digitalWrite(front_right_1, LOW);
      digitalWrite(front_right_2, LOW);
      digitalWrite(rear_right_1, LOW);
      digitalWrite(rear_right_2, LOW);
  }

}
