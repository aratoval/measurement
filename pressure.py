#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import Adafruit_BMP.BMP085 as BMP085

def read_pressure_sensor():
    sensor = BMP085.BMP085()
    print(int(sensor.read_temperature()*10))
    print(sensor.read_pressure())
#    print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
#    print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))

