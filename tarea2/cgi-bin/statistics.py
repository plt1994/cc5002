#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
cgitb.enable()
from utils import render


render("statistics", {})