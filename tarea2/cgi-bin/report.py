#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
cgitb.enable()
from utils import render
from models import region, comuna

def get_data_to_render(display="", confirm_message="", modal_button="", errors=""):
    regiones = region.get_all()
    comunas = comuna.get_all()

    regiones_select = "<option value=0>Seleccione una región</option>"

    for r in regiones:
        regiones_select = f'''
        {regiones_select}
        <option value={r[0]}>{r[1]}</option>
        '''

    json_comunas = {}
    for c in comunas:
        if json_comunas.get(c[2]):
            json_comunas[c[2]].append([c[0], c[1]])
        else:
            json_comunas[c[2]] = [[c[0],c[1]]]

    json_comunas = f"""<script type="text/javascript">
    const COMUNAS = {str(json_comunas)}
    </script>"""
    if not confirm_message:
        confirm_message = "Hemos recibido su información, muchas gracias por colaborar"
    if errors:
        error_details = "<div>"
        for error in errors:
            error_details = f"""
            {error_details}
            <p>{error}</p>
            """
        errors = f"{error_details}</div>"
    data = {
        'regiones': regiones_select,
        'comunas': json_comunas,
        'display': display,
        'confirm_message': confirm_message,
        'modal_button': modal_button,
        'errors': errors
    }
    return data

render("report", get_data_to_render())