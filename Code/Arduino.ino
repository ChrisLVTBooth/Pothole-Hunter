#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;


int motor1pin1 = 6;
int motor1pin2 = 7;

int motor2pin1 = 8;
int motor2pin2 = 9;

int motor1pwm = 5;
int motor2pwm = 10;

int RELAY = 13;

void setup() {
  
  Serial.begin(9600);
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(motor2pin1, OUTPUT);
  pinMode(motor2pin2, OUTPUT);

  pinMode(5, OUTPUT); 
  pinMode(10, OUTPUT);
  pinMode(13, OUTPUT);

  Wire.begin();

//  if (!sensor.init())
//  {
//    Serial.println("Failed to detect and initialize sensor!");
//    while (1) {}
//  }
//  sensor.startContinuous(200);
}

   

void loop() {

 int pwm1 = 180;
 int pwm2 = 150;
 
 char mode = Serial.read(); 
 bool filling = true;

 if (mode == 'I'){
   Serial.println("Start to fill the hole");
   while (filling = true){
   digitalWrite(RELAY, HIGH);
   if(sensor.readRangeContinuousMillimeters() < 60){
   digitalWrite(RELAY, LOW);
   Serial.println("DONE");
   bool filling = false;
   }
   else{
    Serial.println(sensor.readRangeContinuousMillimeters());
    } 
   }
   }

else{
switch (mode) {
//------------------------------
  case 'L': // Motor turn left
  analogWrite(motor1pwm, pwm1);
  analogWrite(motor2pwm, pwm2);

  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, HIGH);

  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, LOW);

  //Serial.println("TURN LEFT"); 
  break;
//------------------------------
  case 'R': // Motor turn right
  analogWrite(motor1pwm, pwm1);
  analogWrite(motor2pwm, pwm2);

  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, LOW);

  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, HIGH);

  //Serial.println("TURN RIGHT"); 
  break;
//------------------------------
  case 'F': // Motor move forward
  analogWrite(motor1pwm, pwm1);
  analogWrite(motor2pwm, pwm2);

  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, HIGH);

  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, HIGH);

  //Serial.println("MOVE FORWARD"); 
  break;
//------------------------------
  case 'S': // Motor STOP
  analogWrite(motor1pwm, pwm1);
  analogWrite(motor2pwm, pwm2);

  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, LOW);

  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, LOW);

  //Serial.println("STOP"); 

  break;
//------------------------------
  case 'H': // Motor move to the hole
  analogWrite(motor1pwm, pwm1);
  analogWrite(motor2pwm, pwm2);

  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, HIGH);

  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, HIGH);

  Serial.println("MOVE TO THE HOLE"); 


  delay(1500);

  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, LOW);

  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, LOW);
  break;
 } 
}
}
