#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import cgitb

cgitb.enable()
from db import doctor

print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
number = 3
form = cgi.FieldStorage()

medicos = doctor.get_doctors()
content = ""

for medico in medicos:
    content=f"""{content}
    <tr>
        <td>{str(medico[1])}</td>
        <td>{str(medico[2])}</td>
        <td>{str(medico[3])}</td>
        <td>{str(medico[5])}</td>
        <td>{str(medico[6])}</td>
    </tr>"""


content = f"""
<table>
<thead>
  <tr>
    <th>Nombre</th>
    <th>Experiencia</th>
    <th>Especialidad</th>
    <th>Email</th>
    <th>Celular</th>
  </tr>
</thead>
<tbody>
  {content}
</tbody>
</table>
"""

head = f"""
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8" /> <!-- Declaring enconding as UTF 8-->
    <title> Ejercicio {number}</title> <!-- Title in pestaña -->
    <link rel="stylesheet" type="text/css" media="screen"  href="../style.css" />    <!-- CSS: -->
</head>
"""
body = f"""
<body>
<ul class="topnav">
  <li><a class="active" href="../index.html">Inicio</a></li>
  <li><a href="../add_doctor.html">Agregar Datos de Médico</a></li>
  <li><a href="list.py">Ver Médicos</a></li>
</ul>

<div id="main">

    <h2>Los datos fueron enviados con éxito!</h2>
    <div class='content'>{content}</div>
    

</div>


</body>
"""

document = f"""
<!-- HTML5 -->
<!DOCTYPE html>
<html lang="es">
{head}
{body}
</html>
"""
print(document, file=utf8stdout)