#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import MySQLdb
import sys

def logining(passwd = str(sys.argv[1])):                # function to log in db - in future maybe it will to be a class
    host = "localhost"
    user = "root"
    dbname ="measurement"
    db = MySQLdb.connect(host, user, passwd, dbname)
    cur = db.cursor()
    return db, cur


def write_to_db(data):                                  # function to write data in to db
    db, cur = logining()
    db.close()

def read_from_db(query):                                # function to read data from db
    db, cur = logining()
    db.close()

def test_db():
    db, cur = logining()
    cur.execute("SELECT version();")
    for i in cur.fetchall():
        print(i)
    db.close()

