#include <SoftwareSerial.h>
#include <Servo.h>

SoftwareSerial nicla(2, 3);  
Servo servo;

int pos = 0;                
int targetPos = 0;          
unsigned long lastMove = 0;  

void setup() {
  Serial.begin(9600);
  nicla.begin(9600);

  servo.attach(9);
  servo.write(pos);  

  Serial.println("UNO ready.");
}

void loop() {


  if (nicla.available()) {
    String msg = nicla.readStringUntil('\n');
    msg.trim();  

    Serial.print("UNO received: ");
    Serial.println(msg);

    if (msg == "1") {
      targetPos = 180;   
    }
    else if (msg == "0") {
      targetPos = 0;     
    }
  }


  unsigned long now = millis();
  if (now - lastMove > 15) {       
    lastMove = now;

    if (pos < targetPos) {
      pos++;
      servo.write(pos);
    }
    else if (pos > targetPos) {
      pos--;
      servo.write(pos);
    }
  }
}