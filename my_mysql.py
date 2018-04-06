#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import MySQLdb


# data config for mysql db
host = "localhost"
user = "root"
passwd = ""
dbname ="measurement"



db = MySQLdb.connect(host, user, passwd, dbname)
cur = db.cursor()

cur.execute("""SELECT version();""")
cur.fetchall()

for i in cur:
    print(i)
