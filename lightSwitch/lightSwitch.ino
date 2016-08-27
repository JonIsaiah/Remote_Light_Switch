/* 
Jon Isaiah earthworm.jim117@gmail.com
Light Switch Code for Interview
*/

#include <Servo.h>

Servo topServo;  // create servo object to control a servo
Servo bottomServo;

int topRestPos = 60; //position for servo to stand clear of switch
int bottomRestPos =140;

int topActivationPos = 110;  //position for servo to activate switch
int bottomActivationPos = 86;

byte data;


void setup() {
  Serial.begin(9600);
  topServo.attach(13);  // attaches the servo on pin 9 to the servo object
  bottomServo.attach(10);

  topServo.write(topRestPos); //send servos to rest postions
  bottomServo.write(bottomRestPos);
  pinMode(9, OUTPUT);
  analogWrite(9, 125);
}

void loop() {

  while (Serial.available() > 0) {    //while 
    data = Serial.read();
    if (data == 49) {

    bottomServo.write(bottomRestPos);
    delay(50);                       //delay a bit for safety
    topServo.write(topActivationPos);    //activate switch from the bottom 
    delay(600);                       // wait for the servo to move              
    topServo.write(topRestPos);   //return the top servo to rest position
    delay(600);   //delay to prevent damage incase of quckly repeated signals
    }

    else if (data == 48) {
      
      topServo.write(topRestPos);       //make sure top servo is out of the way
      delay(50);   //delay a bit for safety
      bottomServo.write(bottomActivationPos);      //activate switch from the bottom
      delay(600);        //wait for the servo to move              
      bottomServo.write(bottomRestPos);   //return the bottom servo to rest position
      delay(600);   //delay to prevent damage incase of quckly repeated signals
    }

    else{
      Serial.println(data);  
    }
    

  }
  
}
