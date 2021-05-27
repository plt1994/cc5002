#!/usr/bin/python3
import re

STATIC_DIR = "../static/"
MEDIA_DIR = "../media/"

def imprimeerror(code, error):
    print(code, error)
    exit()

def validation_check(input_string, regex):
    return bool(re.search(regex, input_string))

def validate_lugar_contacto(lugar, contacto):
    errores = []
    if lugar["region"] == 0:
        errores.append("Debe seleccionar una región")
    if lugar["comuna"] == 0:
        errores.append("Debe seleccionar una comuna")
    if len(lugar["sector"])>100:
        errores.append("El largo máximo del campo 'sector' es de 100")
    if len(contacto["nombre"]) == 0:
        errores.append("El campo nombre es obligatorio")
    if len(contacto["nombre"]) > 200:
        errores.append("El largo máximo del campo nombre es 200")
    if len(contacto["email"]) == 0:
        errores.append("El campo email es obligatorio")
    email_is_valid = validation_check(
        contacto["email"],
        regex='^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
    if not email_is_valid:
        errores.append("El campo email debe tener el formato XXX@YYY.ZZZ")
    if len(contacto["celular"])>0:
        phone_is_valid = validation_check(
            contacto["celular"],
            regex='^\+[1-9]\d{10,14}$')
        if not phone_is_valid:
            errores.append("El campo celular debe tener el formato +56987654321")
    return errores

def validate_lista_avistamientos(lista_a):
    errores = []
    for detail in lista_a:
        date_detail = detail["dia-hora-avistamiento"]
        tipo_detail = detail["tipo-avistamiento"]
        estado_detail = detail["estado-avistamiento"]
        fotos_detail = detail["foto-avistamiento"]
        date_is_valid = validation_check(
            date_detail,
            regex='\d{4}-[01]\d-[0-3]\d [0-2]\d:[0-5]\d')
        if not date_is_valid:
            errores.append("La fecha debe tener un formato de YYYY-MM-DD HH:MM")
        if len(date_detail)<16:
            errores.append("La fecha y hora son requeridas")
        if len(fotos_detail)>5:
            errores.append("El máximo de fotos es 5 por avistamiento")
        if len(fotos_detail)<1:
            errores.append("El mínimo de fotos por avistamiento es 1")
        if tipo_detail == 0:
            errores.append("El tipo es requerido")
        if estado_detail == 0:
            errores.append("El estado es requerido")

def validate_form(form):
    errores = []
    try:
        lista_avistamientos = []
        lugar = {
            "region": form['region'].value,
            "comuna": form['comuna'].value,
            "sector": form['sector'].value if form.getvalue('sector') else ""
        }
        contacto = {
            "nombre": form['nombre'].value,
            "email": form['email'].value,
            "celular": form['celular'].value
        }
        errors_validation_1 = validate_lugar_contacto(lugar, contacto)
        errores = errors_validation_1
        
        
        add_avistamientos = False
        avistamiento = {}
        for val in form.list:
            if val.name == "dia-hora-avistamiento":
                add_avistamientos = True
                if avistamiento.get("tipo-avistamiento") in ['1', '2', '3', '4']:
                    lista_avistamientos.append(avistamiento)
                avistamiento = {}
            if add_avistamientos: 
                if val.name == 'foto-avistamiento':
                    if avistamiento.get(val.name):
                        avistamiento[val.name].append(val)
                    else:
                        avistamiento[val.name] = [val]
                else:
                    avistamiento[val.name] = val.value
        lista_avistamientos.append(avistamiento)
        errores += validate_lista_avistamientos(lista_avistamientos)
        return True, {"lugar": lugar, "contacto": contacto, "lista_avistamientos": lista_avistamientos}
    except Exception as e:
        return False, errores

def render(file, data):
    print("Content-type:text/html\r\n\r\n")
    with open(f'static/{file}.html', 'r') as file:
        s = file.read()
        s = s.replace('script.js',f'{STATIC_DIR}script.js')
        s = s.replace('style.css',f'{STATIC_DIR}style.css')
        s = s.replace('./img/',f'{MEDIA_DIR}')
        # esto parece ser una mala idea por temas de seguridad
        # pero sirve para esta tarea
        s = f'print(f"""{s}""")'
        eval(s)
