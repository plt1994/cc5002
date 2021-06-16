#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
import json

cgitb.enable()
print("Content-type:text/html\r\n\r\n")
from utils import render
from models import detalle_avist

graph_1_data = "''"
graph_2_data = json.dumps(
    [
        { 'label': "No sé",  'data': detalle_avist.count(where="tipo = 'no sé'")},
        { 'label': "Insecto",  'data': detalle_avist.count(where="tipo = 'insecto'")},
        { 'label': "Miriapodo",  'data': detalle_avist.count(where="tipo = 'miriápodo'")},
        { 'label': "Aracnido",  'data': detalle_avist.count(where="tipo = 'arácnido'")}
    ]
)

graph_3_data = "''"

graph_data = f"""
var dataGraph1 = {graph_1_data};
var dataGraph2 = {graph_2_data};
var dataGraph3 = {graph_3_data};
"""

graphjs = (
    """
$(function() {
   """
    + graph_data
    + """
    function graph2() {
        var placeholderGraph2 = $("#placeholder-graph2");
        placeholderGraph2.unbind();
        $("#title").text("Gráfico de torta");
        $("#description").text("Total de avistamientos por tipo.");
        $.plot(placeholderGraph2, dataGraph2, {
            series: {
                pie: {
                    show: true
                }
            }
        });

    };
    graph2();
});
"""
)
data = {"graphjs": graphjs}

render("statistics", data)
