# Sensor-BT
Sensor por conexion bluetooth con grafiica hecha en python entre un ESP32 y un script en python

Para inizializar el programa en Python lo primero es inicializar un entorno virtual (venv) ejecutando el siguiente comando en la terminal

**Windows:**

``` python3 -m venv .venv ```

De esta manera se crea un entorno virtual de python y solo instalamos las librerias necesarias con pip install

``` pip install matplotlib pyserial ```

## Pasos para empezar a utilizar el programa

1. Importamos el codigo de Arduino que está en la carpeta **bluetooth-random-data**.
2. Enlazamos la conexion Bluetooth con el ESP32.
3. Verificamos que el puerto COM sea correcto en el administrador de dispositivos.
4. En la linea 13 de **program.py** cambiamos el puerto COM que corresponda al ESP32 (de ser necesario inicialice repetidamente el programa hasta determinar el puerto correcto).
