# Requisitos de la tarea 3

- [x] Implementación de gráficos dinámicos para la vista de estadísticas
  - [x] gráfico 1: gráfico de lineas para la cantidad de avistamientos por día
    - [x] eje x: días
    - [x] eje y: cantidad avistamientos por día
    - [x] necesito un json con N entradas, cada una con día y cantidad de avistamientos
  - [x] gráfico 2: gráfico de torta para total de avistamientos por tipo
  - [x] gráfico 3: gráfico de barras
    - [x] eje x: meses 
    - [x] eje y: cantidad de avistamientos
    - [x] 3 barras por cada punto en eje x: vivos | muertos | no sé 
    - [x] obtener datos de todos los detalle_avistamiento
      - [x] ordenarlos por tipo
      - [x] ordenarlos por mes
      - [x] parsearlos
- [ ] Implementación de visualización de un mapa en la portada con las comunas que tienen fotos
  - [x] Usar la API de leaflet
  - [x] Incluir marcador por cada comuna con fotos
    - [x] obtener el listado de comunas de los avistamientos con fotos en la base de datos
    - [x] Al pasar el puntero del mouse sobre el marcador, debe aparecer la cantidad de fotos de avistamientos que dicha comuna posee.
      - [x] Esto lo debe hacer usando el atributo “title” del marcador
    - [ ] Al hacer click sobre el marcador que está en el mapa, deberá usar un elemento “popup” de Leaflet para mostrar un listado con las
fotografías de los avistamientos de la comuna correspondiente.
    - [ ]  El listado debe mostrar el día y hora, el tipo de avistamiento y el estado.
    - [ ]  Debe incluir un enlace para “ver avistamiento”, al hacer click sobre el enlace, este se debe abrir una nueva pestaña o ventana
del navegador mostrando la información del avistamiento correspondiente.


# Comandos permisos

- chmod o+rwx media
- chmod o+rx -R static
- chmod 755 -R public_anakena