#include <Adafruit_MAX31865.h>

Adafruit_MAX31865 thermo = Adafruit_MAX31865(8, 14, 16, 15); // Configura los pines CS, DI, DO y CLK según tu conexión.

#define RREF      430.0
#define RNOMINAL  100.0

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit MAX31865 PT100 Sensor Test!");
  thermo.begin(MAX31865_2WIRE);
}

void loop() {
  if (Serial.available() > 0) {
    char request = Serial.read();
    if (request == 'T') {
      float temperature = thermo.temperature(RNOMINAL, RREF);
      
      Serial.println(temperature);

    }
  }
  delay(500);
}
