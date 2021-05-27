#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
cgitb.enable()
from models import avistamiento, detalle_avist, foto, comuna
from utils import render
args = cgi.FieldStorage()
current_page = int(args.getvalue("page", 1))
lista_avistamientos = ""
avistamientos = avistamiento.get_all(limit=5, page=current_page-1, order="ORDER BY dia_hora DESC")
n_of_avistamientos = avistamiento.count()
n_of_pages = int(n_of_avistamientos/5)
pagination = f"""
<div class="pagination"> <a href="?page={current_page-1 if current_page-1>=1 else 1}">&laquo;</a>
"""
for i in range(1, n_of_pages+1):
    if current_page == i:
        pagination=f"""
        {pagination}
        <a href="?page={i}" class="active">{i}</a>
        """
    else:
        pagination = f"""
        {pagination}
        <a href="?page={i}">{i}</a>     
        """
pagination = f"""
{pagination}
<a href="?page={current_page+1 if current_page+1<=n_of_pages else n_of_pages}">&raquo;</a>
</div>
"""

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
    for det_avist in detalles_list:
        cant_fotos+=foto.count(where=f"detalle_avistamiento_id='{det_avist[0]}'")
    lista_avistamientos = f'''
    {lista_avistamientos}
    <div class="fila-insecto clickable" onclick="goToDetail(this)" id={id_avistamiento}>
        <div class="celda">{dia_hora}</div>
        <div class="celda">{comuna_nombre}</div>
        <div class="celda">{sector}</div>
        <div class="celda">{nombre}</div>
        <div class="celda">{cant_avist}</div>
        <div class="celda">{cant_fotos}</div>
    </div>
    '''

data = {
    'lista_avistamientos': lista_avistamientos,
    'pagination': pagination
}

render("list", data)