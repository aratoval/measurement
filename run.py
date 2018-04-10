#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import temperature as t
import pressure as p
import my_mysql as msql

msql.test_db()

temp_probe_id = ["28-0000045d724a", "28-0000045d7be4"]

for i in temp_probe_id:
    t.read_temp(i)

p.read_pressure_sensor()

