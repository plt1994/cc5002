#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector

db = mysql.connector.connect(
    host="anakena",
    user="cc500263_u",
    password="ntesquesus",
)

with open("ejercicio4.sql") as sql_file:
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
