#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector

sql_scripts = ["tarea2.sql", "region-comuna.sql"]
sql_connection_data = {
    "host": "localhost",
    "user": "cc500263_u",
    "password": "ntesquesus",
}
sql_connection_data_dev = {
    "host": "localhost",
    "user": "root",
    "password": "password",
}

db = mysql.connector.connect(**sql_connection_data_dev)

for script in sql_scripts:
    with open(script) as sql_file:
        sql = sql_file.read()
        cursor = db.cursor(dictionary=True)
        result_iterator = cursor.execute(sql, multi=True)
        try:
            for res in result_iterator:
                print("Running query: ", res)
                print(f"Affected {res.rowcount} rows")
        except Exception as e:
            print(e)
        db.commit()
