#include <Arduino.h>
#include "BluetoothSerial.h"

String device_name = "ESP32-BT-Sensor";

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

  // Inicializamos el Bluetooth con el nombre del dispositivo
  SerialBT.begin(device_name);  // Bluetooth nombre del dispositivo

  // Muestra los bytes de datos disponibles en el monitor serial
  Serial.println(SerialBT.available());

}

void loop() {

  if (SerialBT.hasClient()) {
    
    // Generamos un número aleatorio entre 1 y 9
    int x = random(1, 10);

    // En cada loop enviamos linea a linea el dato
    SerialBT.println(x);

    // Imprime en el monitor serial
    Serial.println(x);
  }

  delay(1000);

}
