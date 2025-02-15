#include <ArduinoIoTCloud.h>
#include <Arduino_ConnectionHandler.h>

const char SSID[]     = SECRET_SSID;    
const char PASS[]     = SECRET_OPTIONAL_PASS;

void onAlarmStatusChange();

float accel_x;
float accel_y;
float accel_z;
bool alarm_status;
CloudString alarm_message;  

void initProperties() {
  ArduinoCloud.addProperty(accel_x, READ, ON_CHANGE, NULL);
  ArduinoCloud.addProperty(accel_y, READ, ON_CHANGE, NULL);
  ArduinoCloud.addProperty(accel_z, READ, ON_CHANGE, NULL);
  ArduinoCloud.addProperty(alarm_status, READWRITE, ON_CHANGE, onAlarmStatusChange);
  ArduinoCloud.addProperty(alarm_message, READWRITE, ON_CHANGE, NULL);  
}

WiFiConnectionHandler ArduinoIoTPreferredConnection(SSID, PASS);