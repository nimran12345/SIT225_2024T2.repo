#include <Arduino_LSM6DS3.h>

void setup() {
    Serial.begin(115200);  // Start serial communication
    while (!Serial);       // Wait for Serial connection

    if (!IMU.begin()) {
        Serial.println("Failed to initialize IMU!");
        while (1);
    }
    
    Serial.println("Gyroscope initialized. Collecting data...");
}

void loop() {
    float x, y, z;

    if (IMU.gyroscopeAvailable()) {
        IMU.readGyroscope(x, y, z);
        Serial.print(millis()); // Timestamp
        Serial.print(",");
        Serial.print(x, 6);
        Serial.print(",");
        Serial.print(y, 6);
        Serial.print(",");
        Serial.println(z, 6);
    }

    delay(100);  // Adjust sampling rate (10Hz)
}

