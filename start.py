#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import temperature as t
import pressure as p
import humidity as h
import my_mysql as msql
import time


delta = 20.0

temp_probe_id = ["28-0000045d724a", "28-0000045d7be4"]
sensor_id_name = {temp_probe_id[0]:"na zewnątrz", temp_probe_id[1]:"w domu"}


#while 1:
for step in range(int(60.0 / delta)):
    start_time = time.time()
    time_to_db = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
#    print(time_to_db)
    for i in temp_probe_id:
        temp = t.read_temp(i)
        query = """INSERT INTO temperature (Date_and_Time, Sensor_Id, VALUE) VALUES ('{}', '{}', {});""".format(time_to_db, i, temp)
        msql.write_to_db(query)

    temp_pressure, pressure = p.read_pressure_sensor()
    query = """INSERT INTO pressure (Date_and_Time, Sensor_Id, pressure, temperature) VALUES ('{}', '{}', {}, {});""".format(time_to_db, "BMP085", pressure, temp_pressure)
    msql.write_to_db(query)

    temp_humidity, humidity = h.read_humidity_sensor()
    query = """INSERT INTO humidity (Date_and_Time, Sensor_Id, humidity, temperature) VALUES ('{}', '{}', {}, {});""".format(time_to_db, "DHT11", humidity, temp_humidity)
    msql.write_to_db(query)

    d = time.time() - start_time
    if d < delta:
        time.sleep(delta - d)
