#include <Servo.h>
Servo myservo;
int pos = 0;
int val = 0;
int sensorValue = 0;
long t = 0, ti = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  myservo.attach(32);
 
  ti = millis();


}

void loop() {
  // put your main code here, to run repeatedly:
  t = millis() - ti; //currenttime=initial
  sensorValue = analogRead(35);
  Serial.print(t);
  Serial.print(",");
  Serial.print(sensorValue);
  Serial.println();
  delay(10);
  if (Serial.available())
  {
    int input = Serial.parseInt();
    if (input == 1)
    {
      myservo.write(0);
    }
    else
    {
      myservo.write(115);
    }
  }
}
