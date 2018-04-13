# measurement

Measurement using Raspberry pi

# Requirements

You mast install:

* Adafruit DHT11 library

git clone https://github.com/adafruit/Adafruit_Python_DHT.git

cd Adafruit_Python_DHT

sudo apt-get install build-essential python3-dev

sudo python3 setup.py install

* Adafruit_Python_BMP library

git clone https://github.com/adafruit/Adafruit_Python_BMP.git

cd Adafruit_Python_BMP

sudo apt-get install python3-smbus

sudo python3 setup.py install

* for security

sudo apt-get install libffi-dev libssl-dev -y

sudo pip3 install bcrypt

# Run

If you want start (after config) put in console (you are must been in script root folder):

python3 run.py your_passwd_to_database
