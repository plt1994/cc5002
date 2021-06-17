async function putMarks(mapObject){
	$.ajax({
		url: "comunas_markers.py"
	}).done(function(data) {
        avistamientos = JSON.parse(data)
        comunas = avistamientos.comunas
        console.log(typeof avistamientos)
		$.ajax({
            url: "../static/chile.json"
        }).done(function(data) {
            // FIXME: hay un error con las comunas que tienen espacios en el nombre
            // no coinciden con las de la base de datos
            for (let i = 0; i < data.length; i++) {
                if (comunas.includes(data[i].name)){
                    var dataComuna = avistamientos.data[data[i].name]
                    var marker = L.marker(
                        [data[i].lat, data[i].lng],
                        {
                            title: "fotos: "+dataComuna.nfotos}).addTo(mymap);
                    marker.bindPopup("<b>Hello world!</b><br>aqui van las img.");
                    
                }
                
            }
            // $("#myDiv").empty();
            // $( "#myDiv" ).append("<pre>"+ data +"</pre>");
        });
	});
}