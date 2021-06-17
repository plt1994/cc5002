#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
import json
cgitb.enable()
print("Content-type:text/html\r\n\r\n")
from models import avistamiento, foto, comuna, detalle_avist

#necesito todas las comunas que tienen foto
#veo cuales son los detalle_avistamiento con foto
#para cada uno obtengo el avistamiento
#para cada avistamiento obtengo el id comuna
#con el id comuna obtengo el nombre de la comuna
#con el nombre de la comuna hago match con chile.json
#obtengo latitud y longitud de cada comuna


lista_avistamientos = {
    "comunas": [],
    "data": {}
}
avistamiento_count = avistamiento.count()
avistamientos = avistamiento.get_all(limit=avistamiento_count+1, page=0, order="ORDER BY dia_hora DESC")
n_of_avistamientos = avistamiento.count()
n_of_pages = int(n_of_avistamientos/5)


for av in avistamientos:
    id_avistamiento = av[0]
    comuna_id = av[1]
    dia_hora = av[2]
    sector = av[3]
    nombre = av[4]
    comuna_nombre = comuna.get_by_id(comuna_id)[0][1]
    detalles_list = detalle_avist.get_by_id(id_avistamiento)
    cant_avist = len(detalles_list)
    cant_fotos = 0
    detalles_avistamientos = []
    for det_avist in detalles_list:
        cant_fotos+=foto.count(where=f"detalle_avistamiento_id='{det_avist[0]}'")
        if cant_fotos>0:
            lista_avistamientos["comunas"].append(comuna_nombre)
            aux = {
                    "det_avistamiento": {
                        "diaHora": str(det_avist[1]),
                        "tipo": det_avist[2],
                        "estado": det_avist[3],
                        "idAvistamiento": id_avistamiento,
                        "fotos": foto.get_by_id(det_avist[0])
                    },
                    "cantidadFotos": cant_fotos,
                }
            detalles_avistamientos.append(aux)
    for detalle_avistamiento_i in detalles_avistamientos:
        if lista_avistamientos["data"].get(comuna_nombre):
            lista_avistamientos["data"][comuna_nombre].append(detalle_avistamiento_i)
        else:
            lista_avistamientos["data"][comuna_nombre] = [detalle_avistamiento_i]
    
    lista_avistamientos["comunas"] = list(set(lista_avistamientos["comunas"]))

print(json.dumps(lista_avistamientos))