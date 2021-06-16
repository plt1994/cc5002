# Requisitos de la tarea 3

- [ ] Implementación de gráficos dinámicos para la vista de estadísticas
  - [ ] gráfico 1: gráfico de lineas para la cantidad de avistamientos por día
    - [ ] eje x: días
    - [ ] eje y: cantidad avistamientos por día
    - [ ] necesito un json con N entradas, cada una con día y cantidad de avistamientos
  - [ ] gráfico 2: gráfico de torta para total de avistamientos por tipo
  - [ ] gráfico 3: gráfico de barras
    - [ ] eje x: meses 
    - [ ] eje y: cantidad de avistamientos
    - [ ] 3 barras por cada punto en eje x: vivos | muertos | no sé 
- [ ] Implementación de visualización de un mapa en la portada con las comunas que tienen fotos
  - [ ] Usar la API de leaflet
  - [ ] Incluir marcador por cada comuna con fotos
    - [ ] obtener el listado de comunas de los avistamientos con fotos en la base de datos
    - [ ] Al pasar el puntero del mouse sobre el marcador, debe aparecer la cantidad de fotos de avistamientos que dicha comuna posee.
      - [ ] Esto lo debe hacer usando el atributo “title” del marcador
    - [ ] Al hacer click sobre el marcador que está en el mapa, deberá usar un elemento “popup” de Leaflet para mostrar un listado con las
fotografías de los avistamientos de la comuna correspondiente.
    - [ ]  El listado debe mostrar el día y hora, el tipo de avistamiento y el estado.
    - [ ]  Debe incluir un enlace para “ver avistamiento”, al hacer click sobre el enlace, este se debe abrir una nueva pestaña o ventana
del navegador mostrando la información del avistamiento correspondiente.