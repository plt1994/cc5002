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

draw_map = """
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(mymap);
"""

n_of_markers = 5

mapa =f"""
<div id="mapid"></div>
<script>

	var mymap = L.map('mapid').setView([-33.4, -70.6], 13);
    putMarks(mymap)

	{draw_map}

</script>
"""

data = {
    "insectos_table": insectos_table,
    "mapa": mapa
}

render("index", data)