#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
import json

cgitb.enable()
print("Content-type:text/html\r\n\r\n")
from utils import render
from models import detalle_avist
meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
estado_avist = {
    "no sé": {"Enero":0,
            "Febrero":0,
            "Marzo":0,
            "Abril":0,
            "Mayo":0,
            "Junio":0,
            "Julio":0,
            "Agosto":0,
            "Septiembre":0,
            "Octubre":0,
            "Noviembre":0,
            "Diciembre":0},
    "vivo": {"Enero":0,
            "Febrero":0,
            "Marzo":0,
            "Abril":0,
            "Mayo":0,
            "Junio":0,
            "Julio":0,
            "Agosto":0,
            "Septiembre":0,
            "Octubre":0,
            "Noviembre":0,
            "Diciembre":0},
    "muerto":{"Enero":0,
            "Febrero":0,
            "Marzo":0,
            "Abril":0,
            "Mayo":0,
            "Junio":0,
            "Julio":0,
            "Agosto":0,
            "Septiembre":0,
            "Octubre":0,
            "Noviembre":0,
            "Diciembre":0}
}
total_d_a = detalle_avist.count()
detalle_avist_data = detalle_avist.get_all(limit=total_d_a, order="ORDER BY dia_hora")
avistamientos_por_dia = {}
for avist in detalle_avist_data:
    dia = avist[1].strftime("%m/%d/%y")
    if avistamientos_por_dia.get(dia):
        avistamientos_por_dia[dia] += 1
    else:
        avistamientos_por_dia[dia] = 1
    estado_avist[avist[3]][meses[avist[1].month]]+=1

graph_1_data = json.dumps(list(avistamientos_por_dia.items()))
print(graph_1_data)
graph_2_data = json.dumps(
    [
        { 'label': "No sé",  'data': detalle_avist.count(where="tipo = 'no sé'")},
        { 'label': "Insecto",  'data': detalle_avist.count(where="tipo = 'insecto'")},
        { 'label': "Miriapodo",  'data': detalle_avist.count(where="tipo = 'miriápodo'")},
        { 'label': "Aracnido",  'data': detalle_avist.count(where="tipo = 'arácnido'")}
    ]
)

avist_estado = {
    "nose": json.dumps(list(estado_avist["no sé"].items())),
    "vivo": json.dumps(list(estado_avist["vivo"].items())),
    "muerto": json.dumps(list(estado_avist["muerto"].items()))
}

graph_3_data = f"""
var dataGraph3Nose = {avist_estado["nose"]};
var dataGraph3Vivo = {avist_estado["vivo"]};
var dataGraph3Muerto = {avist_estado["muerto"]};
"""

graph_data = f"""
var dataGraph1 = {graph_1_data};
var dataGraph2 = {graph_2_data};
{graph_3_data}
"""

graphjs = (
    """
$(function() {
   """
    + graph_data
    + """

    function graph1() {
        var placeholderGraph1 = $("#placeholder-graph1");
        placeholderGraph1.unbind();
        $("#title-0").text("Cantidad de avistamientos por día");
        $.plot(placeholderGraph1, [{
            data : dataGraph1,
            lines: { show: true },
			points: { show: true }
            }],
            {
                xaxis: {
                    axisLabel: 'día',
                    mode: "categories",
                    showTicks: true,
                    gridLines: true
                    },
                yaxis: {
                    axisLabel: 'cantidad de avistamientos'
                }
            });

    };

    function graph2() {
        var placeholderGraph2 = $("#placeholder-graph2");
        placeholderGraph2.unbind();
        $("#title-1").text("Total de avistamientos por tipo");
        $.plot(placeholderGraph2, dataGraph2, {
            series: {
                pie: {
                    show: true
                }
            }
        });

    };

    var stack = 0,
	bars = true;  
    var dataGraph3 = [
        {color: "gray", bars: {show: true, barWidth: 0.3}, data: dataGraph3Nose, label: "No sé"},
        {color: "green", bars: {show: true, barWidth: 0.2}, data: dataGraph3Vivo, label: "Vivo"},
        {color: "red", bars: {show: true, barWidth: 0.1}, data: dataGraph3Muerto, label: "Muerto"},
        ];

        
        var legendSettings = {
				position: "nw",
                show: true,
                noColumns: 2,
                container: null
            };
    function graph3(){
        var placeholderGraph3 = $("#placeholder-graph3");
        placeholderGraph3.unbind();
        $("#title-2").text("Estado de avistamientos por mes");
		$.plot(placeholderGraph3, 
			dataGraph3
			, {
                legend: legendSettings,
                series: {
					bars: {
						show: bars,
						barWidth: 0.6
					}
				},
			xaxis: {
                axisLabel: 'meses',
                label: "meses",
				mode: "categories",
				categories: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
				showTicks: true,
				gridLines: true
			},
            yaxis: {
                axisLabel: 'cantidad'
            }
		});
    }

    graph1();
    graph2();
    graph3();
});
"""
)
data = {"graphjs": graphjs}

render("statistics", data)
