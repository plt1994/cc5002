#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import hashlib
from utils import imprimeerror
import os
import filetype

ENV = "prod"

MAX_FILE_SIZE = 10000 * 1000  # 10 MB
sql_connection_data = {
    "host": "localhost",
    "user": "cc500263_u",
    "password": "ntesquesus",
    "database": "cc500263_db"
}

sql_connection_data_dev = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "tarea2"
}

if ENV == "dev":
    db_connection_data = sql_connection_data_dev
else:
    db_connection_data = sql_connection_data

class Model:
    save_query = ""
    table = ''
    id_for_query = "id"

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def save(self, data):
        data = tuple(data)
        sql = self.save_query
        self.cursor.execute(sql, data)
        self.db.commit()
        return self.cursor.lastrowid

    def get_all(self, limit=500, page=0, order=""):
        self.cursor.execute(f"SELECT * FROM {self.table} {order} LIMIT {limit} OFFSET {page*limit}")
        return self.cursor.fetchall()

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE {self.id_for_query}='{id}'")
        return self.cursor.fetchall()

    def count(self, where=None):
        sql = f"SELECT COUNT(id) FROM {self.table}"
        if where:
            sql = f"{sql} WHERE {where}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

class Region(Model):
    table = "region"

class Foto(Model):
    save_query = '''
    INSERT INTO foto (ruta_archivo, nombre_archivo, detalle_avistamiento_id)
    VALUES ( %s, %s, %s)
    '''
    table = "foto"
    id_for_query = "detalle_avistamiento_id"

    def save_file(self, fileobj):
        filename = fileobj.filename

        if not filename:
            imprimeerror(10, 'Archivo no subido')

        # calculamos cuantos elementos existen y actualizamos el hash
        sql = "SELECT COUNT(id) FROM foto"
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1  # peligroso
        hash_archivo = str(total) + hashlib.sha256(filename.encode()).hexdigest()[0:30]

        # guardar el archivo
        file_path = f'./media/{hash_archivo}.png'
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
        return hash_archivo, filename

    def save(self, data):
        fileobj = data[0]
        detalle_avistamiento_id = data[1]
        foto_path, foto_name  = self.save_file(fileobj)
        data = [
            foto_path,
            foto_name,
            detalle_avistamiento_id
        ]
        return super().save(data)

class DetalleAvistamiento(Model):
    save_query = '''
    INSERT INTO detalle_avistamiento (dia_hora, tipo, estado, avistamiento_id)
    VALUES (%s, %s, %s, %s)
    '''
    table = "detalle_avistamiento"
    id_for_query = "avistamiento_id"

class Comuna(Model):
    table = "comuna"

class Avistamiento(Model):
    save_query = '''
    INSERT INTO avistamiento (comuna_id, dia_hora, sector, nombre, email, celular) 
    VALUES (%s, %s, %s, %s, %s, %s)
    '''
    table = "avistamiento"

    def get_last_five(self):
        sql = '''
        SELECT DA.dia_hora, CO.nombre, AV.sector, DA.tipo, FT.nombre_archivo, FT.ruta_archivo
        FROM avistamiento AV, detalle_avistamiento DA, comuna CO, foto FT
        WHERE DA.avistamiento_id = AV.id AND AV.comuna_id=CO.id
        AND DA.id = FT.detalle_avistamiento_id
        ORDER BY DA.dia_hora DESC
        LIMIT 5
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

region = Region(**db_connection_data)
comuna = Comuna(**db_connection_data)
avistamiento = Avistamiento(**db_connection_data)
detalle_avist = DetalleAvistamiento(**db_connection_data)
foto = Foto(**db_connection_data)