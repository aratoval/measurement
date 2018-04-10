#!/usr/bin/env python3
# -*- coding:utf-8 -*-


probe_path = "/sys/bus/w1/devices/"
probe_id = ["28-0000045d724a", "28-0000045d7be4"]

def read_temp(probe_id=probe_id[0]):
    print(open(probe_path + probe_id + "/w1_slave", "r").read().replace("\n","")[68:])

