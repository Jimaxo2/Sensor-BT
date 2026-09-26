#include <Arduino.h>
#include "BluetoothSerial.h"

String device_name = "ESP32-BT-Jimmy";

// Check if Bluetooth is available
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

// Check Serial Port Profile
#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Port Profile for Bluetooth is not available or not enabled. It is only available for the ESP32 chip.
#endif

BluetoothSerial SerialBT;

void setup() {

  Serial.begin(115200);
  SerialBT.begin(device_name);  //Bluetooth device name
  //SerialBT.deleteAllBondedDevices(); // Uncomment this to delete paired devices; Must be called after begin
  Serial.printf("The device with name \"%s\" is started.\nNow you can pair it with Bluetooth!\n", device_name.c_str());

  Serial.println(SerialBT.available());

}

void loop() {

  Serial.println(SerialBT.hasClient());
  if (SerialBT.hasClient()) {
    
    int x = random(1, 10);

    // probar print o write alguno debe funcionar
    SerialBT.println(x);

    Serial.write(x);
    Serial.println(x);
  }

  delay(1000);

}
