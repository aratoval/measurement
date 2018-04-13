#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#import sys
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

pin = 17

def read_humidity_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return int(temperature * 10), int(humidity * 10)
    else:
        return "dupa z pomiaru"
