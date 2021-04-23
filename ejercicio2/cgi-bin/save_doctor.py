#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import cgitb

cgitb.enable()

print("Content-type:text/html\r\n\r\n")

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
number = 3
form = cgi.FieldStorage()
content = ""

for key in form.keys():
    campo = key.replace("-medico", "").capitalize()
    content=f"""
<div class='leyenda'>{campo}:
<div class='value'>{form[key].value}</div></div>
{content}"""

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