#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb

cgitb.enable()

print("Content-type:text/html\r\n\r\n")


html = """
<html>
    <body>
        <h1>Hola mundo</h1>
    </body>
</html>
"""

print(html)