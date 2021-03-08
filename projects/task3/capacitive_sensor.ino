#include "CapacitiveSensor.h"

// The time to spend on setup in milliseconds
const int setupDuration = 6000;
// The amount of samples per capacitive sensor read
const int sensorSamples = 10;

const int ledPin = 11;
const int debugPin = 13;

CapacitiveSensor capSensor = CapacitiveSensor(4, 2);

// These will hold the max/min outputs of the sensor when setup is done
long maxValue = 10000;
long minValue = 1000;

void setup() {
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
  pinMode(debugPin, OUTPUT);

  // Spend time on determining the min/max values for the sesnsor output
  // This requires the user to touch and release the sensor while the debug led is on
  digitalWrite(debugPin, HIGH);
  while(millis() < setupDuration) {
    long sensorValue = capSensor.capacitiveSensor(sensorSamples);
    if(sensorValue < minValue) {
      minValue = sensorValue;
    }
    if(sensorValue > maxValue) {
      maxValue = sensorValue;
    }
  }
  digitalWrite(debugPin, LOW);

  Serial.print("Min value is ");
  Serial.println(minValue);
  Serial.print("Max value is ");
  Serial.println(maxValue);
}

void loop() {
  long sensorValue = capSensor.capacitiveSensor(sensorSamples);

  // Map the sensor value to an analog output value based on the min/max values calculated from setup
  int ledOutput = map(sensorValue, minValue, maxValue, 0, 255);

  // Make sure that output value does not surpass analogue limits, this can happen when the sensor gives a value outside min/max values
  ledOutput = min(max(ledOutput, 0), 255);
  
  analogWrite(ledPin, ledOutput);
  
  Serial.println(ledOutput);
}
