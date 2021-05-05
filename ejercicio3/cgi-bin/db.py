#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector


class Doctor:

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def save_doctor(self, data):
        sql = '''
            INSERT INTO medico (nombre, experiencia, especialidad, foto, email, celular)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        self.cursor.execute(sql, data)
        self.db.commit()

    def get_doctors(self):
        self.cursor.execute(f"SELECT * FROM medico")
        return self.cursor.fetchall()


doctor = Doctor("localhost", "root", "password", "ejercicio3")