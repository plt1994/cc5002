#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
cgitb.enable()
print("Content-type:text/html\r\n\r\n")
from models import avistamiento
from utils import STATIC_DIR, MEDIA_DIR, render
from environment import ENV

last_avistamientos = avistamiento.get_last_five()

insectos_table_Example = '''
    <div class="fila-insecto">
        <div class="celda">20-02-2021 13:27</div>
        <div class="celda">Calera de Tango</div>
        <div class="celda">Los bajos</div>
        <div class="celda">arácnido</div>
        <div class="celda"><img src="./img/araña-pollito.jpg" alt="imagen de araña"></div>
    </div>
    '''

insectos_table = ""

for avist in last_avistamientos:
    insectos_table = f'''
    {insectos_table}
    <div class="fila-insecto">
        <div class="celda">{avist[0]}</div>
        <div class="celda">{avist[1]}</div>
        <div class="celda">{avist[2]}</div>
        <div class="celda">{avist[3]}</div>
        <div class="celda"><img src="{MEDIA_DIR}/{avist[5]}.png" alt="{avist[4]}"></div>
    </div>
    '''

data = {
    "insectos_table": insectos_table
}

render("index", data)