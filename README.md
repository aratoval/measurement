# What this scrept does.

Measurement temperature, humidity, pressure using Raspberry pi and sensors.

This sensors are

*DS18B20 digital thermometer

BMP085 barometric pressure sensor

DHT11 Humidity Sensor* 

# Prerequisites

* Adafruit DHT11 library
```
    git clone https://github.com/adafruit/Adafruit_Python_DHT.git

    cd Adafruit_Python_DHT

    sudo apt-get install build-essential python3-dev

    sudo python3 setup.py install
```
* Adafruit_Python_BMP library
```
    git clone https://github.com/adafruit/Adafruit_Python_BMP.git

    cd Adafruit_Python_BMP

    sudo apt-get install python3-smbus

    sudo python3 setup.py install
```
* for security::
```
    sudo apt-get install libffi-dev libssl-dev -y

    sudo pip3 install bcrypt
```
# Start script

After configuration to start the script execute
```
    python3 start.py your_passwd_to_database
```
