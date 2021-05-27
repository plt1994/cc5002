#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
cgitb.enable()
from models import avistamiento, foto, comuna, detalle_avist
from utils import render, MEDIA_DIR

args = cgi.FieldStorage()

try:
    id_avistamiento = int(args.getvalue("id"))
    av = avistamiento.get_by_id(id_avistamiento)[0]
    comuna_id = av[1]
    dia_hora = av[2]
    sector = av[3]
    nombre = av[4]
    comuna_nombre = comuna.get_by_id(comuna_id)[0][1]
    detalles_list = detalle_avist.get_by_id(id_avistamiento)
    cant_avist = len(detalles_list)
    detalles_todos_avistamientos = ""
    detalles = f"""
    <div class="detalle formulario" id="main">
        <div class="entrada">
            <div class="leyenda">Nombre contacto:</div>
            <div class="leyenda-detalle">{nombre}</div>
        </div>
        <div class="entrada">
            <div class="leyenda">Comuna:</div>
            <div class="leyenda-detalle">{comuna_nombre}</div>
        </div>
        <div class="entrada">
            <div class="leyenda">Sector:</div>
            <div class="leyenda-detalle">{sector}</div>
        </div>
        <div class="entrada">
            <div class="leyenda">Fecha - hora:</div>
            <div class="leyenda-detalle">{dia_hora}</div>
        </div>    
        <div class="entrada">
            <div class="leyenda">Total avistamientos:</div>
            <div class="leyenda-detalle">{cant_avist}</div>
        </div>
    """
    for det_avist in detalles_list:
        imagenes = ""
        fotos=foto.get_by_id(det_avist[0])
        for f in fotos:
            imagenes = f"""
            {imagenes}
            <div class="celda clickable" onclick="showImg(this)" id="{f[0]}"><img src="{MEDIA_DIR}{f[1]}.png" alt="{f[2]}"></div>
            """
        detalles_todos_avistamientos = f"""
            <div class="entrada">
                <div class="leyenda">Tipo:</div>
                <div class="leyenda-detalle">{det_avist[2]}</div>
            </div>
            <div class="entrada">
                <div class="leyenda">Estado:</div>
                <div class="leyenda-detalle">{det_avist[3]}</div>
            </div>
            <div class="entrada">
                <div class="leyenda">Total Fotos:</div>
                <div class="leyenda-detalle">{len(fotos)}</div>
            </div>
            <div class="imagenes-holder">
                {imagenes}
            </div>
        """
    detalles = f"""
    {detalles}
    {detalles_todos_avistamientos}
    </div>
    """
    data = {
        "detalles": detalles,
    }
    render("detail", data)
except Exception as e:
    render("detail", {})