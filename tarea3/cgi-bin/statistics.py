#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
cgitb.enable()
print("Content-type:text/html\r\n\r\n")
from utils import render


render("statistics", {})