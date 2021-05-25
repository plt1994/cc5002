#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import hashlib
from utils import imprimeerror
import os
import filetype

MAX_FILE_SIZE = 10000 * 1000  # 10 MB


class Doctor:

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def save_file(self, fileobj):
        #codigo basado en la solucion del aux 5
        filename = fileobj.filename

        if not filename:
            imprimeerror(10, 'Archivo no subido')

        # verificamos el tipo
        size = os.fstat(fileobj.file.fileno()).st_size
        if size > MAX_FILE_SIZE:
            imprimeerror(1000, 'Tamaño excede 10mb')

        # calculamos cuantos elementos existen y actualizamos el hash
        sql = "SELECT COUNT(id) FROM archivo"
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1  # peligroso
        hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

        # guardar el archivo
        file_path = f'../media/{hash_archivo}.png'
        open(file_path, 'wb').write(fileobj.file.read())

        # verificamos el tipo, si no es valido lo borramos de la db
        tipo = filetype.guess(file_path)
        if tipo.mime != 'image/png':
            os.remove(file_path)
            imprimeerror(40, 'Tipo archivo no es png')

        # guardamos la imagen en la db
        sql = """
            INSERT INTO archivo (nombre, path)
            VALUES (%s, %s)
        """
        self.cursor.execute(sql, (filename, hash_archivo))
        self.db.commit()  # id
        id_archivo = self.cursor.getlastrowid()
        return id_archivo

    def save_doctor(self, data):
        fileobj = data[3]
        file_id = self.save_file(fileobj)
        data[3] = file_id
        data = tuple(data)
        sql = '''
            INSERT INTO medico (nombre, experiencia, especialidad, foto, email, celular)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        self.cursor.execute(sql, data)
        self.db.commit()

    def get_doctors(self):
        self.cursor.execute(f"SELECT * FROM medico")
        return self.cursor.fetchall()
    
    def get_foto(self, id):
        self.cursor.execute(f"SELECT * FROM archivo WHERE id='{id}'")
        return self.cursor.fetchall()


doctor = Doctor("localhost", "root", "password", "ejercicio4")