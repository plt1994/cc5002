#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
cgitb.enable()
from models import avistamiento, detalle_avist, foto
from utils import render, validate_form
from report import get_data_to_render

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
form = cgi.FieldStorage()

form_is_valid, cleaned_data = validate_form(form)

if form_is_valid:
    data_avistamento = [
        cleaned_data["lugar"]["comuna"],
        "2021-05-01 22:22",
        cleaned_data["lugar"]["sector"],
        cleaned_data["contacto"]["nombre"],
        cleaned_data["contacto"]["email"],
        cleaned_data["contacto"]["celular"]
    ]
    id_avistamiento = avistamiento.save(data_avistamento)
    for detalle in cleaned_data["lista_avistamientos"]:
        data_detalle_avistamiento = [
            detalle["dia-hora-avistamiento"],
            detalle["tipo-avistamiento"],
            detalle["estado-avistamiento"],
            id_avistamiento
        ]
        id_detalle_avistamiento = detalle_avist.save(data_detalle_avistamiento)
        for foto_avistamiento in detalle["foto-avistamiento"]:
            data_foto = [
                foto_avistamiento,
                id_detalle_avistamiento
            ]
            foto.save(data_foto)
    finish = """
    <button type="button" onclick="moveTo('index')">Volver al inicio</button>
    """
    render("report", get_data_to_render(display='style="display: block;"', modal_button=finish))
else:
    errors = cleaned_data
    go_back = """
        <button type="button" onclick="window.history.back()">Volver</button>
    """
    render("report", get_data_to_render(display='style="display: block;"', modal_button=go_back, errors=errors, confirm_message="Oops! al parecer tu formulario tiene algunos errores"))